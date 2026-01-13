"""
BeatNet Warm-up Module

PURPOSE: Pre-approve BeatNet binary with macOS XProtect at app startup
CONTEXT: XProtect scans binaries on first execution, causing 40+ second delays.
         Running a quick dummy analysis at startup "warms up" the binary.

WHY: First real beat detection will run at full speed (~30s for 33s audio)
     instead of timing out or taking 46+ seconds due to XProtect scanning.
"""

from __future__ import annotations

from pathlib import Path
import tempfile
import threading
import time
import numpy as np
import soundfile as sf
import subprocess
from typing import Optional

from utils.logger import get_logger
from utils.beat_service_client import analyze_beats, is_beat_service_available, _terminate_process

logger = get_logger()

# Global state for warm-up synchronization
_warmup_lock = threading.Lock()
_warmup_complete = False
_warmup_in_progress = False

# Global subprocess tracking for cancellation
_warmup_process: Optional[subprocess.Popen] = None
_warmup_process_lock = threading.Lock()
_warmup_cancelled = threading.Event()


def generate_dummy_audio(
    duration: float = 1.0, sample_rate: int = 44100
) -> tuple[np.ndarray, int]:
    """
    Generate dummy audio for BeatNet warm-up.

    Args:
        duration: Duration in seconds (default: 1.0)
        sample_rate: Sample rate in Hz (default: 44100)

    Returns:
        Tuple of (audio_data, sample_rate)

    WHY: Simple sine wave at 120 BPM is sufficient to trigger BeatNet analysis
    """
    num_samples = int(duration * sample_rate)

    # Generate simple sine wave at 120 BPM (2 Hz for beats)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    frequency = 2.0  # 2 Hz = 120 BPM
    audio = 0.3 * np.sin(2 * np.pi * frequency * t)  # Moderate amplitude

    return audio.astype(np.float32), sample_rate


def warmup_beatnet_service(timeout: float = 240.0) -> bool:
    """
    Warm up BeatNet service by running a quick dummy analysis.

    This triggers XProtect scanning on the first run, so subsequent
    real analyses can run at full speed.

    Args:
        timeout: Maximum time to wait for warm-up analysis (default: 240s)
                 Increased to handle XProtect delays, resource contention
                 (e.g., when separation is running), and system load.
                 Warmup is non-critical and runs in background, so longer
                 timeout is acceptable.

    Returns:
        True if warm-up successful, False if failed or BeatNet unavailable

    WHY: Prevents 40+ second XProtect delays on first real beat detection.
         Longer timeout handles resource contention when other processes
         (e.g., separation) are using MPS/GPU simultaneously.
    """
    global _warmup_complete, _warmup_in_progress, _warmup_process

    # Reset cancellation flag for new warmup attempt
    _warmup_cancelled.clear()

    with _warmup_lock:
        # Skip if already complete
        if _warmup_complete:
            logger.debug("BeatNet warm-up already complete, skipping")
            return True

        # Skip if already in progress
        if _warmup_in_progress:
            logger.debug("BeatNet warm-up already in progress, skipping")
            return False

        _warmup_in_progress = True

    try:
        # Check cancellation before starting
        if _warmup_cancelled.is_set():
            logger.debug("BeatNet warm-up cancelled before starting")
            with _warmup_lock:
                _warmup_complete = True
                _warmup_in_progress = False
            return False

        # Check if BeatNet service is available
        if not is_beat_service_available():
            logger.info("BeatNet service not available, skipping warm-up")
            with _warmup_lock:
                _warmup_complete = True  # Mark as complete to avoid retries
                _warmup_in_progress = False
            return False

        logger.info("Starting BeatNet warm-up analysis...")

        try:
            # Generate 1-second dummy audio
            audio_data, sample_rate = generate_dummy_audio(duration=1.0)

            # Save to temporary file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)

            sf.write(str(tmp_path), audio_data, sample_rate)

            try:
                # Callback to track subprocess for cancellation
                def track_process(process: subprocess.Popen) -> None:
                    global _warmup_process
                    with _warmup_process_lock:
                        _warmup_process = process

                # Run BeatNet analysis (this will trigger XProtect on first run)
                # Pass callback to track subprocess for cancellation
                result = analyze_beats(
                    tmp_path,
                    timeout_seconds=timeout,
                    device="auto",
                    process_callback=track_process,
                )

                # Clear subprocess reference after completion
                with _warmup_process_lock:
                    _warmup_process = None

                # Check if cancelled (subprocess may have been terminated)
                if _warmup_cancelled.is_set():
                    logger.debug("BeatNet warm-up was cancelled")
                    with _warmup_lock:
                        _warmup_complete = True
                        _warmup_in_progress = False
                    return False

                # Success! BeatNet is now "approved" by XProtect
                logger.info(
                    f"BeatNet warm-up complete: {result.tempo:.1f} BPM, "
                    f"{len(result.beats)} beats detected in {result.analysis_duration:.1f}s"
                )

                with _warmup_lock:
                    _warmup_complete = True
                    _warmup_in_progress = False

                return True

            except Exception as e:
                # Clear subprocess reference on error
                with _warmup_process_lock:
                    _warmup_process = None

                # Check if error was due to cancellation
                if _warmup_cancelled.is_set():
                    logger.debug("BeatNet warm-up cancelled during execution")
                    with _warmup_lock:
                        _warmup_complete = True
                        _warmup_in_progress = False
                    return False

                # Warm-up failed, but this is non-critical
                # First real analysis will still work, just slower
                logger.warning(f"BeatNet warm-up failed (non-critical): {e}")
                with _warmup_lock:
                    _warmup_complete = True  # Mark as complete to avoid retries
                    _warmup_in_progress = False
                return False

            finally:
                # Clean up temporary file
                if tmp_path.exists():
                    tmp_path.unlink()
                # Ensure subprocess reference is cleared
                with _warmup_process_lock:
                    _warmup_process = None

        except Exception as e:
            logger.error(f"Unexpected error in warm-up: {e}", exc_info=True)
            with _warmup_lock:
                _warmup_complete = True  # Mark as complete to avoid retries
                _warmup_in_progress = False
            return False

    except Exception as e:
        logger.error(f"Unexpected error in warm-up: {e}", exc_info=True)
        with _warmup_lock:
            _warmup_complete = True  # Mark as complete to avoid retries
            _warmup_in_progress = False
        return False


def cancel_warmup() -> None:
    """
    Cancel ongoing BeatNet warm-up and terminate subprocess if running.

    PURPOSE: Allow graceful shutdown when user quits app during warmup
    CONTEXT: Called from closeEvent() or aboutToQuit signal to prevent freeze
             when XProtect is scanning the beatnet-service binary

    WHY: Prevents 1-2 minute freeze when user quits immediately after startup
    """
    global _warmup_process

    # Set cancellation flag
    _warmup_cancelled.set()
    logger.debug("BeatNet warm-up cancellation requested")

    # Terminate subprocess if running
    with _warmup_process_lock:
        if _warmup_process is not None:
            try:
                logger.info("Terminating BeatNet warm-up subprocess...")
                _terminate_process(_warmup_process)
                logger.debug("BeatNet warm-up subprocess terminated")
            except Exception as e:
                logger.warning(f"Error terminating warm-up subprocess: {e}")
            finally:
                _warmup_process = None


def warmup_beatnet_async():
    """
    Warm up BeatNet service asynchronously (non-blocking).

    This can be called from the GUI thread without blocking.
    Use QThreadPool to run in background.

    WHY: Don't block app startup, but still get the warm-up benefit
    """
    from PySide6.QtCore import QRunnable, QThreadPool

    class WarmupRunnable(QRunnable):
        def run(self):
            warmup_beatnet_service()

    # Schedule warm-up in background thread pool
    # WHY: Runs silently in background, user won't notice
    QThreadPool.globalInstance().start(WarmupRunnable())
    logger.debug("BeatNet warm-up scheduled in background")


def wait_for_warmup_complete(max_wait_seconds: float = 120.0) -> bool:
    """
    Wait for BeatNet warm-up to complete before starting real analysis.

    This ensures XProtect scanning happens during warm-up, not during
    the first real beat detection. Runs silently without user notification.

    Args:
        max_wait_seconds: Maximum time to wait (default: 120s)
                          Increased for M1 and less performant Macs

    Returns:
        True if warm-up complete, False if timeout or not started

    WHY: Prevents race condition where real detection starts before warm-up
    """
    global _warmup_complete, _warmup_in_progress

    # Quick check first - if already complete, return immediately
    with _warmup_lock:
        if _warmup_complete:
            logger.debug("Warm-up already complete, proceeding immediately")
            return True

    # Only wait if warm-up is in progress
    start_time = time.time()
    check_interval = 0.2  # Check every 200ms to avoid busy-waiting

    while True:
        with _warmup_lock:
            if _warmup_complete:
                logger.debug("Warm-up complete, proceeding with real analysis")
                return True

            if not _warmup_in_progress:
                # Warm-up not started yet, give it a moment
                elapsed = time.time() - start_time
                if elapsed < 1.0:
                    # Give warm-up a chance to start (first second)
                    pass
                else:
                    # Warm-up not started after 1s, proceed anyway
                    logger.debug("Warm-up not started, proceeding without wait")
                    return False

        # Check timeout
        elapsed = time.time() - start_time
        if elapsed >= max_wait_seconds:
            logger.debug(
                f"Warm-up timeout after {elapsed:.1f}s, proceeding with real analysis"
            )
            return False

        # Wait before checking again (non-blocking sleep)
        time.sleep(check_interval)
