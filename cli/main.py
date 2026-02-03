#!/usr/bin/env python3
"""
StemLooper CLI - Main entry point

Separates audio into stems and exports loops for samplers.
"""

import sys
from pathlib import Path

import click
from tqdm import tqdm

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from cli.pipeline import StemLooperPipeline


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--stems",
    type=click.Choice(["4", "6"]),
    default="6",
    help="Number of stems: 4 (vocals, drums, bass, other) or 6 (+piano, guitar)",
)
@click.option(
    "--bars",
    type=click.Choice(["2", "4", "8"]),
    default="4",
    help="Bars per loop chunk",
)
@click.option(
    "--bpm",
    type=int,
    default=None,
    help="Override detected BPM (auto-detect if not specified)",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    default=None,
    help="Output directory (default: ./output)",
)
@click.option(
    "--format",
    "file_format",
    type=click.Choice(["wav", "flac", "aiff"]),
    default="wav",
    help="Output audio format",
)
@click.option(
    "--sample-rate",
    type=click.Choice(["44100", "48000"]),
    default="44100",
    help="Output sample rate",
)
@click.option(
    "--bit-depth",
    type=click.Choice(["16", "24", "32"]),
    default="24",
    help="Output bit depth",
)
@click.option(
    "--skip-separation",
    is_flag=True,
    help="Skip separation (use existing stems in output/stems/)",
)
@click.option(
    "--skip-loops",
    is_flag=True,
    help="Skip loop export (only separate stems)",
)
@click.option(
    "--device",
    type=click.Choice(["auto", "cpu", "mps", "cuda"]),
    default="auto",
    help="Processing device (auto-detect recommended)",
)
def main(
    input_file: Path,
    stems: str,
    bars: str,
    bpm: int,
    output: Path,
    file_format: str,
    sample_rate: str,
    bit_depth: str,
    skip_separation: bool,
    skip_loops: bool,
    device: str,
):
    """
    Separate audio into stems and export loops for samplers.

    INPUT_FILE: Audio file to process (mp3, wav, flac, etc.)

    \b
    Examples:
        stemlooper track.mp3
        stemlooper track.mp3 --stems 6 --bars 4
        stemlooper track.mp3 --bpm 128 --output ./export
        stemlooper track.mp3 --skip-separation  # Use existing stems
    """
    click.echo()
    click.secho("=" * 50, fg="cyan")
    click.secho("  StemLooper CLI", fg="cyan", bold=True)
    click.secho("=" * 50, fg="cyan")
    click.echo()

    # Setup output directory
    if output is None:
        output = Path("./output")

    output = output.resolve()

    # Display configuration
    click.echo(f"  Input:       {input_file.name}")
    click.echo(f"  Output:      {output}")
    click.echo(f"  Stems:       {stems}")
    click.echo(f"  Bars/loop:   {bars}")
    click.echo(f"  BPM:         {bpm if bpm else 'auto-detect'}")
    click.echo(f"  Format:      {file_format.upper()} {bit_depth}-bit @ {sample_rate}Hz")
    click.echo(f"  Device:      {device}")
    click.echo()

    # Create pipeline
    pipeline = StemLooperPipeline(
        input_file=input_file,
        output_dir=output,
        num_stems=int(stems),
        bars_per_loop=int(bars),
        bpm_override=bpm,
        file_format=file_format.upper(),
        sample_rate=int(sample_rate),
        bit_depth=int(bit_depth),
        device=device,
    )

    try:
        # Step 1: Stem Separation
        if not skip_separation:
            click.secho("[1/3] Stem Separation", fg="yellow", bold=True)
            with tqdm(total=100, desc="Separating", unit="%", ncols=80) as pbar:
                def progress_cb(msg: str, pct: int):
                    pbar.set_description(msg[:30])
                    pbar.n = pct
                    pbar.refresh()

                stems_dir = pipeline.separate_stems(progress_callback=progress_cb)

            click.secho(f"  ✓ Stems saved to: {stems_dir}", fg="green")
            click.echo()
        else:
            click.secho("[1/3] Stem Separation (skipped)", fg="yellow")
            stems_dir = output / "stems"
            if not stems_dir.exists():
                click.secho(f"  ✗ Error: {stems_dir} not found", fg="red")
                sys.exit(1)
            click.echo()

        # Step 2: Beat Detection
        click.secho("[2/3] Beat Detection", fg="yellow", bold=True)
        detected_bpm, confidence = pipeline.detect_bpm()

        if bpm:
            click.echo(f"  Using override BPM: {bpm}")
        else:
            conf_str = f" ({confidence:.0%})" if confidence else ""
            click.secho(f"  ✓ Detected BPM: {detected_bpm:.1f}{conf_str}", fg="green")
        click.echo()

        # Step 3: Loop Export
        if not skip_loops:
            click.secho("[3/3] Loop Export", fg="yellow", bold=True)

            with tqdm(total=100, desc="Exporting", unit="%", ncols=80) as pbar:
                def loop_progress_cb(msg: str, pct: int):
                    pbar.set_description(msg[:30])
                    pbar.n = pct
                    pbar.refresh()

                results = pipeline.export_loops(progress_callback=loop_progress_cb)

            # Summary
            total_files = sum(r.chunk_count for r in results.values() if r.success)
            loops_dir = output / "loops"
            click.secho(f"  ✓ Exported {total_files} loop files to: {loops_dir}", fg="green")
            click.echo()

            # Per-stem summary
            for stem_name, result in results.items():
                if result.success:
                    click.echo(f"    {stem_name}: {result.chunk_count} files")
                else:
                    click.secho(f"    {stem_name}: FAILED - {result.error_message}", fg="red")
        else:
            click.secho("[3/3] Loop Export (skipped)", fg="yellow")

        click.echo()
        click.secho("=" * 50, fg="green")
        click.secho("  Done!", fg="green", bold=True)
        click.secho("=" * 50, fg="green")
        click.echo()

    except KeyboardInterrupt:
        click.echo()
        click.secho("Interrupted by user", fg="yellow")
        sys.exit(130)
    except Exception as e:
        click.echo()
        click.secho(f"Error: {e}", fg="red")
        sys.exit(1)


if __name__ == "__main__":
    main()
