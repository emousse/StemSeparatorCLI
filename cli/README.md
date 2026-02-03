# StemLooper CLI

Command-line interface for audio stem separation and loop export.

## Features

- **Stem Separation**: Split audio into 4 or 6 stems using Demucs v4
- **BPM Detection**: Auto-detect tempo using DeepRhythm/librosa
- **Loop Export**: Export stems as musically-timed loops for samplers

## Installation

```bash
# From the project root
pip install -r requirements.txt

# Or install click separately if needed
pip install click>=8.0.0
```

## Usage

### Basic Usage

```bash
# Separate into 6 stems and export 4-bar loops
python stemlooper.py track.mp3

# Specify stems and bars
python stemlooper.py track.mp3 --stems 6 --bars 4

# With custom output directory
python stemlooper.py track.mp3 --output ./my_export
```

### Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--stems` | 4, 6 | 6 | Number of stems to separate |
| `--bars` | 2, 4, 8 | 4 | Bars per loop chunk |
| `--bpm` | integer | auto | Override auto-detected BPM |
| `--output`, `-o` | path | ./output | Output directory |
| `--format` | wav, flac, aiff | wav | Audio format |
| `--sample-rate` | 44100, 48000 | 44100 | Sample rate |
| `--bit-depth` | 16, 24, 32 | 24 | Bit depth |
| `--device` | auto, cpu, mps, cuda | auto | Processing device |
| `--skip-separation` | flag | - | Skip separation, use existing stems |
| `--skip-loops` | flag | - | Only separate, skip loop export |

### Examples

```bash
# Full pipeline with 6 stems and 4-bar loops
python stemlooper.py song.mp3 --stems 6 --bars 4

# Force BPM (useful when auto-detection fails)
python stemlooper.py song.mp3 --bpm 128

# Only separate stems (no loops)
python stemlooper.py song.mp3 --skip-loops

# Only export loops (stems already exist)
python stemlooper.py song.mp3 --skip-separation

# Export as FLAC with 8-bar loops
python stemlooper.py song.mp3 --format flac --bars 8

# Use CPU instead of GPU
python stemlooper.py song.mp3 --device cpu
```

## Output Structure

```
output/
├── stems/
│   ├── song_(Vocals)_htdemucs_6s.wav
│   ├── song_(Drums)_htdemucs_6s.wav
│   ├── song_(Bass)_htdemucs_6s.wav
│   ├── song_(Guitar)_htdemucs_6s.wav
│   ├── song_(Piano)_htdemucs_6s.wav
│   └── song_(Other)_htdemucs_6s.wav
└── loops/
    ├── song_vocals_120BPM_4T_01.wav
    ├── song_vocals_120BPM_4T_02.wav
    ├── song_drums_120BPM_4T_01.wav
    ├── song_drums_120BPM_4T_02.wav
    └── ...
```

### Filename Convention

```
<name>_<stem>_<BPM>BPM_<bars>T_<NN>.<ext>

Example: MySong_vocals_120BPM_4T_01.wav
         │       │      │     │  │
         │       │      │     │  └── Chunk number (01-99)
         │       │      │     └───── Bars per chunk (T = Takte)
         │       │      └─────────── Detected/specified BPM
         │       └────────────────── Stem name
         └────────────────────────── Original filename
```

## Models

| Stems | Model | Size | Description |
|-------|-------|------|-------------|
| 4 | htdemucs | ~160 MB | Vocals, Drums, Bass, Other |
| 6 | htdemucs_6s | ~240 MB | + Piano, Guitar |

Models are downloaded automatically on first use.

## BPM Detection

The CLI uses a fallback chain for BPM detection:

1. **DeepRhythm** (primary) - ~95% accuracy, provides confidence score
2. **librosa** (fallback) - ~80% accuracy

For best results:
- Use `--bpm` flag if you know the tempo
- Check the confidence percentage in output
- Confidence < 70% suggests manual BPM override

## Performance

| Hardware | 5-min track (6 stems) |
|----------|----------------------|
| Apple M1 (MPS) | ~3-4 minutes |
| Apple M2/M3 (MPS) | ~2-3 minutes |
| NVIDIA GPU (CUDA) | ~1-2 minutes |
| CPU only | ~10-15 minutes |

## Troubleshooting

### "Model not found"
Models are downloaded to `/tmp/audio-separator-models/`. Ensure you have internet access on first run.

### Low BPM confidence
Use `--bpm` to specify the correct tempo manually.

### Out of memory
Try `--device cpu` or process shorter files.

### Stems not found (--skip-separation)
Ensure stems exist in `<output>/stems/` directory.

## Architecture

```
cli/
├── __init__.py      # Package init
├── main.py          # Click CLI entry point
├── pipeline.py      # Orchestration logic
└── README.md        # This file

stemlooper.py        # Entry script (project root)
```

The CLI reuses existing modules:
- `core/sampler_export.py` - Loop export with zero-crossing
- `utils/beat_detection.py` - BPM detection
- `utils/audio_processing.py` - Audio utilities
- `utils/loop_math.py` - Musical calculations
