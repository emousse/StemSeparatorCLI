"""
StemLooper Pipeline - Orchestrates stem separation and loop export

Reuses existing core modules:
- core/separator.py for stem separation
- utils/beat_detection.py for BPM detection
- core/sampler_export.py for loop export
"""

import os
import sys
from pathlib import Path
from typing import Optional, Callable, Dict, Tuple

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from utils.logger import get_logger
from core.sampler_export import export_sampler_loops, ExportResult

logger = get_logger()


class StemLooperPipeline:
    """
    Pipeline for stem separation and loop export.

    Workflow:
    1. Separate audio into stems (Demucs 4 or 6 stems)
    2. Detect BPM (DeepRhythm/librosa)
    3. Export each stem as loops (N bars per chunk)
    """

    # Model mapping for audio-separator (use .yaml extension)
    MODEL_MAP = {
        4: "htdemucs.yaml",      # 4 stems: vocals, drums, bass, other
        6: "htdemucs_6s.yaml",   # 6 stems: + piano, guitar
    }

    STEM_NAMES = {
        4: ["vocals", "drums", "bass", "other"],
        6: ["vocals", "drums", "bass", "guitar", "piano", "other"],
    }

    def __init__(
        self,
        input_file: Path,
        output_dir: Path,
        num_stems: int = 6,
        bars_per_loop: int = 4,
        bpm_override: Optional[int] = None,
        file_format: str = "WAV",
        sample_rate: int = 44100,
        bit_depth: int = 24,
        device: str = "auto",
    ):
        """
        Initialize the pipeline.

        Args:
            input_file: Path to input audio file
            output_dir: Base output directory
            num_stems: 4 or 6 stems
            bars_per_loop: 2, 4, or 8 bars per loop chunk
            bpm_override: Override auto-detected BPM
            file_format: WAV, FLAC, or AIFF
            sample_rate: 44100 or 48000
            bit_depth: 16, 24, or 32
            device: auto, cpu, mps, or cuda
        """
        self.input_file = Path(input_file).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.num_stems = num_stems
        self.bars_per_loop = bars_per_loop
        self.bpm_override = bpm_override
        self.file_format = file_format.upper()
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth
        self.device = device

        # Derived paths
        self.stems_dir = self.output_dir / "stems"
        self.loops_dir = self.output_dir / "loops"

        # State
        self._detected_bpm: Optional[float] = None
        self._bpm_confidence: Optional[float] = None
        self._stem_files: Dict[str, Path] = {}

        # Create directories
        self.stems_dir.mkdir(parents=True, exist_ok=True)
        self.loops_dir.mkdir(parents=True, exist_ok=True)

    def separate_stems(
        self,
        progress_callback: Optional[Callable[[str, int], None]] = None,
    ) -> Path:
        """
        Separate audio into stems using audio-separator.

        Args:
            progress_callback: Optional callback(message, percent)

        Returns:
            Path to stems directory
        """
        from audio_separator.separator import Separator

        model_name = self.MODEL_MAP[self.num_stems]

        logger.info(f"Separating {self.input_file.name} with {model_name}")

        if progress_callback:
            progress_callback("Loading model...", 5)

        # Determine device
        device = self._get_device()

        # Initialize separator
        separator = Separator(
            output_dir=str(self.stems_dir),
            output_format=self.file_format,
        )

        if progress_callback:
            progress_callback("Loading model...", 10)

        # Load model
        separator.load_model(model_name)

        if progress_callback:
            progress_callback("Separating audio...", 20)

        # Run separation
        output_files = separator.separate(str(self.input_file))

        if progress_callback:
            progress_callback("Finalizing...", 90)

        # Map output files to stem names
        self._map_stem_files(output_files)

        if progress_callback:
            progress_callback("Done", 100)

        logger.info(f"Separation complete: {len(output_files)} stems")
        return self.stems_dir

    def _map_stem_files(self, output_files: list) -> None:
        """Map output files to stem names."""
        for file_path in output_files:
            path = Path(file_path)
            # Ensure absolute path
            if not path.is_absolute():
                path = self.stems_dir / path.name

            name_lower = path.stem.lower()

            for stem_name in self.STEM_NAMES[self.num_stems]:
                if stem_name in name_lower:
                    self._stem_files[stem_name] = path
                    break

        logger.info(f"Mapped stems: {list(self._stem_files.keys())}")

    def _get_device(self) -> str:
        """Determine processing device."""
        if self.device != "auto":
            return self.device

        # Auto-detect
        try:
            import torch
            if torch.backends.mps.is_available():
                return "mps"
            elif torch.cuda.is_available():
                return "cuda"
        except ImportError:
            pass

        return "cpu"

    def detect_bpm(self) -> Tuple[float, Optional[float]]:
        """
        Detect BPM from stems (preferably drums stem).

        Returns:
            Tuple of (bpm, confidence)
        """
        if self.bpm_override:
            self._detected_bpm = float(self.bpm_override)
            self._bpm_confidence = None
            return self._detected_bpm, None

        from utils.audio_processing import detect_bpm
        import soundfile as sf
        import numpy as np

        # Prefer drums stem for BPM detection
        bpm_source = None
        for stem_name in ["drums", "bass", "vocals"]:
            if stem_name in self._stem_files:
                bpm_source = self._stem_files[stem_name]
                break

        # Fallback to any stem or original file
        if bpm_source is None:
            if self._stem_files:
                bpm_source = list(self._stem_files.values())[0]
            else:
                bpm_source = self.input_file

        logger.info(f"Detecting BPM from: {bpm_source.name}")

        # Load audio
        audio_data, sample_rate = sf.read(str(bpm_source), always_2d=False)
        if audio_data.ndim > 1:
            audio_data = np.mean(audio_data, axis=1)

        # Detect BPM
        bpm, confidence = detect_bpm(audio_data, sample_rate)

        if bpm <= 0:
            bpm = 120.0
            confidence = None
            logger.warning("BPM detection failed, using default 120")

        self._detected_bpm = bpm
        self._bpm_confidence = confidence

        logger.info(f"Detected BPM: {bpm:.1f} (confidence: {confidence})")
        return bpm, confidence

    def export_loops(
        self,
        progress_callback: Optional[Callable[[str, int], None]] = None,
    ) -> Dict[str, ExportResult]:
        """
        Export all stems as loops.

        Args:
            progress_callback: Optional callback(message, percent)

        Returns:
            Dict mapping stem names to ExportResult
        """
        if self._detected_bpm is None:
            self.detect_bpm()

        bpm = self.bpm_override or int(round(self._detected_bpm))
        results = {}

        # Find stem files if not already mapped
        if not self._stem_files:
            self._find_stem_files()

        total_stems = len(self._stem_files)
        common_filename = self.input_file.stem

        for idx, (stem_name, stem_path) in enumerate(self._stem_files.items()):
            # Calculate progress per stem
            base_progress = int((idx / total_stems) * 100)

            if progress_callback:
                progress_callback(f"Exporting {stem_name}...", base_progress)

            logger.info(f"Exporting loops for {stem_name}: {stem_path.name}")

            # Export loops for this stem
            result = export_sampler_loops(
                input_path=stem_path,
                output_dir=self.loops_dir,
                bpm=bpm,
                bars=self.bars_per_loop,
                sample_rate=self.sample_rate,
                bit_depth=self.bit_depth,
                channels=2,  # Stereo
                file_format=self.file_format,
                common_filename=common_filename,
                stem_name=stem_name,
            )

            results[stem_name] = result

            if result.success:
                logger.info(f"  {stem_name}: {result.chunk_count} loops exported")
            else:
                logger.error(f"  {stem_name}: FAILED - {result.error_message}")

        if progress_callback:
            progress_callback("Done", 100)

        return results

    def _find_stem_files(self) -> None:
        """Find stem files in stems directory."""
        if not self.stems_dir.exists():
            return

        for stem_name in self.STEM_NAMES[self.num_stems]:
            # Look for files containing stem name
            for ext in ["wav", "flac", "aiff"]:
                pattern = f"*{stem_name}*.{ext}"
                matches = list(self.stems_dir.glob(pattern))
                if matches:
                    self._stem_files[stem_name] = matches[0]
                    break

            # Also try capitalized version
            if stem_name not in self._stem_files:
                for ext in ["wav", "flac", "aiff"]:
                    pattern = f"*{stem_name.capitalize()}*.{ext}"
                    matches = list(self.stems_dir.glob(pattern))
                    if matches:
                        self._stem_files[stem_name] = matches[0]
                        break

        logger.info(f"Found stem files: {list(self._stem_files.keys())}")

    def run(
        self,
        progress_callback: Optional[Callable[[str, int], None]] = None,
    ) -> Dict[str, ExportResult]:
        """
        Run the complete pipeline.

        Args:
            progress_callback: Optional callback(message, percent)

        Returns:
            Dict mapping stem names to ExportResult
        """
        # Step 1: Separate
        self.separate_stems(progress_callback)

        # Step 2: Detect BPM
        self.detect_bpm()

        # Step 3: Export loops
        return self.export_loops(progress_callback)
