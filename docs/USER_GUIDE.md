# Stem Separator - User Guide

This comprehensive guide will help you get started with Stem Separator and make the most of its features.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Main Window Overview](#main-window-overview)
3. [Separating Audio Files](#separating-audio-files)
4. [Recording System Audio](#recording-system-audio)
5. [Playing and Mixing Stems](#playing-and-mixing-stems)
6. [Exporting Audio](#exporting-audio)
7. [Settings and Preferences](#settings-and-preferences)
8. [Tips and Best Practices](#tips-and-best-practices)
9. [Troubleshooting](#troubleshooting)

---

## Getting Started

### First Launch

When you launch Stem Separator for the first time:

1. **macOS Security**: If you see a security warning, right-click the app icon and select "Open"
2. **Models Download**: The app will automatically download AI models when you first use a separation feature (this may take a few minutes)
3. **Permissions**: If you plan to use the recording feature:
   - **macOS 13+**: Grant "Screen Recording" permission when prompted
   - **macOS 12 and earlier**: The app will guide you through installing BlackHole

### Basic Workflow

The typical workflow is:
1. **Load** audio (file upload or recording)
2. **Separate** into stems (vocals, drums, bass, etc.)
3. **Play** and mix stems
4. **Export** your mix

---

## Main Window Overview

The Stem Separator window has four main tabs:

### 1. Upload Tab
- Load audio files for separation
- Choose AI models and quality settings
- Start separation process

### 2. Recording Tab
- Record system audio from your Mac
- No external cables needed
- Direct recording from any application

### 3. Queue Tab
- View and manage separation jobs
- Monitor progress
- Cancel or retry operations

### 4. Player Tab
- Load and play separated stems
- Mix stems with individual volume controls
- Export mixed audio

---

## Separating Audio Files

### Basic Separation

1. **Navigate to Upload Tab**
   - Click the "Upload" tab at the top of the window

2. **Load Audio File**
   - **Drag & Drop**: Drag an audio file directly into the window
   - **File Browser**: Click "Select Audio File" and browse for your file
   - Supported formats: WAV, MP3, FLAC, M4A, OGG, AAC

3. **Choose a Model**
   - **Mel-RoFormer** (Recommended): Best quality for vocals
   - **BS-RoFormer**: Excellent all-around quality
   - **Demucs v4 (6-stem)**: Separates piano and guitar as well
   - **Demucs v4 (4-stem)**: Faster, good quality
   - **MDX-Net**: Strong for vocals and lead instruments

4. **Select Separation Mode**
   - **4-Stem**: Vocals, Drums, Bass, Other
   - **6-Stem**: Vocals, Drums, Bass, Piano, Guitar, Other (Demucs only)
   - **2-Stem (Karaoke)**: Vocals, Instrumental

5. **Click "Separate"**
   - The job will appear in the Queue tab
   - Progress is shown with a progress bar
   - Processing time varies by file length and model

6. **Find Your Stems**
   - Stems are saved in: `temp/separated/[filename]/[model_name]/`
   - Each stem is a separate WAV file

### Ensemble Separation (Maximum Quality)

For professional applications where quality is critical:

1. **Check "Ensemble Mode"** in the Upload tab

2. **Choose Ensemble Configuration**:
   - **Balanced** (~2x slower): Good balance of quality and speed
   - **Quality** (~2.5x slower): Professional quality (recommended)
   - **Ultra** (~3.5x slower): Maximum possible quality

3. **How It Works**:
   - Ensemble mode uses multiple AI models
   - Vocals are processed first using 2-3 models combined
   - Remaining stems (drums, bass, other) are then processed
   - Results are blended for superior quality

4. **When to Use**:
   - Professional music production
   - Critical vocal extraction
   - When quality matters more than speed
   - Final masters and releases

### Understanding Processing Time

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| Demucs v4 (4-stem) | Fast | Good | Quick separations |
| Mel-RoFormer | Medium | Excellent | Vocal extraction |
| BS-RoFormer | Medium | Excellent | All-around quality |
| Demucs v4 (6-stem) | Medium | Very Good | Piano/Guitar separation |
| Balanced Ensemble | Slow (2x) | Superior | Professional work |
| Quality Ensemble | Slower (2.5x) | Excellent | Critical applications |
| Ultra Ensemble | Slowest (3.5x) | Maximum | Final masters |

**Note**: Times are approximate and depend on:
- File length (longer files = more processing)
- Your hardware (Apple Silicon M1/M2/M3 is fastest)
- GPU availability (GPU is much faster than CPU)

### Large Files (>30 Minutes)

For files longer than 30 minutes:
- The app automatically splits the file into 5-minute chunks
- Each chunk is processed separately
- Results are seamlessly combined
- No quality loss from chunking

---

## Recording System Audio

Stem Separator can record audio playing on your Mac without any cables or additional hardware.

### macOS 13+ (Ventura and Later) - Recommended Method

1. **Navigate to Recording Tab**

2. **Grant Screen Recording Permission** (first time only)
   - Click "Start Recording"
   - macOS will prompt for "Screen Recording" permission
   - Open System Settings → Privacy & Security → Screen Recording
   - Enable permission for Stem Separator
   - Restart the app

3. **Start Recording**
   - Click "Start Recording"
   - The recording indicator will show (red icon)
   - No input device selection needed

4. **Play Your Audio**
   - Play music, videos, or any audio on your Mac
   - All system audio is captured automatically
   - Quality: 44.1 kHz, stereo, lossless

5. **Stop and Save**
   - Click "Stop & Save"
   - Choose a filename and location
   - The recording is saved as WAV file

6. **Separate the Recording**
   - The recorded file can be used immediately in the Upload tab

### macOS 12 and Earlier - BlackHole Method

1. **Install BlackHole** (first time only)
   - The app will offer to install BlackHole automatically
   - Or manually: `brew install blackhole-2ch`

2. **Navigate to Recording Tab**

3. **Select Input Device**
   - In the device dropdown, select "BlackHole 2ch"

4. **Configure macOS Audio** (one-time setup)
   - Open "Audio MIDI Setup" (in Applications → Utilities)
   - Create a "Multi-Output Device"
   - Check both your speakers and "BlackHole 2ch"
   - In System Settings → Sound, select this Multi-Output Device
   - This allows you to hear audio while recording

5. **Start Recording**
   - Click "Start Recording" in Stem Separator
   - Play your audio source
   - Click "Stop & Save" when finished

### Recording Tips

- **Quality**: Always record at the highest quality available in your source
- **Silence**: Remove silence at the beginning/end by trimming the audio file
- **Volume**: Keep your system volume at a comfortable level (50-80%)
- **Avoid Clipping**: If the recording is distorted, lower the system volume
- **Background Noise**: Close other applications to reduce CPU load and potential audio glitches

---

## Playing and Mixing Stems

After separation, use the Player tab to listen to and mix your stems.

### Loading Stems

**Method 1: Load Full Session**
1. Click "Load Stems"
2. Navigate to your separated stems folder
3. Select any file in the folder
4. All stems in that folder are loaded automatically

**Method 2: Load Individual Stems**
1. Click "Add Stem"
2. Select individual stem files
3. Repeat for each stem you want to load

### Player Controls

#### Playback Controls
- **Play/Pause**: Start or pause playback
- **Stop**: Stop playback and return to beginning
- **Position Slider**: Drag to seek to any position in the audio

#### Stem Mixer

Each stem has its own controls:

- **Volume Slider**: Adjust the loudness of each stem (0-100%)
- **M (Mute)**: Silence this stem while hearing others
- **S (Solo)**: Hear only this stem (mutes all others)
- **Stem Label**: Shows the stem name (Vocals, Drums, etc.)

#### Master Controls
- **Master Volume**: Overall volume control for all stems
- **Waveform Display**: Visual representation of the audio
- **Time Display**: Current position and total duration

### Mixing Tips

1. **Start with All Stems**: Load all stems and play the original mix first
2. **Isolate Stems**: Use Solo (S) to hear each stem individually
3. **Find Problems**: Use Mute (M) to identify which stem has issues
4. **Create Variations**:
   - **Karaoke**: Mute vocals
   - **Acapella**: Solo vocals only
   - **Instrumental Focus**: Lower vocals, raise drums/bass
   - **Practice Track**: Mute your instrument to play along

5. **Balance Levels**: Adjust volume sliders so no stem is too loud or too quiet
6. **Reference Original**: Occasionally play the original file to compare

### Keyboard Shortcuts

- **Space**: Play/Pause
- **Escape**: Stop
- **Arrow Keys**: Seek position
- **M**: Mute selected stem
- **S**: Solo selected stem

---

## Exporting Audio

### Exporting Mixed Stems

1. **Load and Mix Stems** in the Player tab
2. **Adjust Volumes** to your desired mix
3. **Click "Export Mixed"**
4. **Choose Settings**:
   - **Format**: WAV (lossless) or MP3 (compressed)
   - **Sample Rate**: 44100 Hz (CD quality) or 48000 Hz (professional)
   - **Bit Depth** (WAV only): 16-bit (standard) or 24-bit (professional)
   - **MP3 Bitrate**: 128, 192, 256, or 320 kbps
5. **Select Output Location** and filename
6. **Click "Export"**

### Export Use Cases

| Export Format | Best For |
|---------------|----------|
| WAV 16-bit 44.1kHz | CD masters, final exports |
| WAV 24-bit 48kHz | Professional audio production |
| MP3 320kbps | High-quality sharing, streaming |
| MP3 192kbps | Good quality, smaller file size |
| MP3 128kbps | Web use, demos (not recommended for masters) |

### Loop/Sample Export (Advanced)

For music producers who want to create loops or samples:

1. **Enable Loop Detection** in the Export Loops widget
2. **Set Beat Detection Parameters**:
   - **Minimum Loop Length**: Shortest acceptable loop (in beats)
   - **Maximum Loop Length**: Longest acceptable loop (in beats)
3. **Export Loops**:
   - The app analyzes the audio for rhythmic patterns
   - Loops are automatically detected and extracted
   - Each loop is saved as a separate file
4. **Output Formats**:
   - Individual WAV files for each loop
   - Sampler-compatible format (Ableton, Maschine, etc.)

---

## Settings and Preferences

### Accessing Settings

- **Menu Bar**: Stem Separator → Settings (⌘,)
- **Or**: Click the settings icon in the main window

### Available Settings

#### Language
- **German (Deutsch)**: Full German interface
- **English**: Full English interface

#### GPU Acceleration
- **Enable GPU**: Use Apple Silicon (MPS) or NVIDIA (CUDA) for faster processing
- **Disable GPU**: Force CPU mode (useful for troubleshooting)

#### Default Model
- Choose which AI model is selected by default

#### Quality Preset
- **Fast**: Quick separation, good quality
- **Standard**: Balanced quality and speed (default)
- **High**: Better quality, slower
- **Ultra**: Maximum quality, slowest

#### Output Directory
- Choose where separated stems are saved
- Default: `temp/separated/`

#### Audio Settings
- **Sample Rate**: 44100 Hz (default) or 48000 Hz
- **Channels**: Stereo (2 channels)

---

## Tips and Best Practices

### Getting the Best Results

1. **Use High-Quality Source Files**
   - WAV or FLAC files are better than MP3
   - Higher bitrate MP3s (320kbps) work better than lower bitrates
   - Avoid highly compressed or low-quality sources

2. **Choose the Right Model**
   - **For Vocals**: Mel-RoFormer or Ensemble Mode
   - **For Drums**: BS-RoFormer or Demucs
   - **For Piano/Guitar**: Demucs v4 (6-stem)
   - **For Speed**: Demucs v4 (4-stem)
   - **For Quality**: Quality Ensemble or Ultra Ensemble

3. **Manage Your Time**
   - Processing can take several minutes for long files
   - Use Queue tab to process multiple files overnight
   - Start with shorter files to test quality

4. **Organize Your Files**
   - Rename output folders to keep track of separations
   - Use descriptive names for exported mixes
   - Keep original files for re-processing with different models

5. **Experiment**
   - Try different models on the same file
   - Compare results to find what works best for your use case
   - Ensemble modes often provide noticeably better quality

### Hardware Recommendations

**For Best Performance:**
- **Apple Silicon Mac (M1/M2/M3)**: Fastest processing with MPS acceleration
- **16 GB RAM or more**: Handles large files and ensemble modes smoothly
- **SSD Storage**: Faster file I/O during processing

**Minimum Requirements:**
- **Intel Mac**: Works but slower (especially ensemble modes)
- **8 GB RAM**: Adequate for most files, may struggle with very long files
- **GPU Disabled**: Falls back to CPU (much slower but still works)

### Common Workflows

#### Workflow 1: Creating Karaoke Tracks
1. Load song in Upload tab
2. Select any model
3. Choose "2-Stem (Karaoke)" mode
4. Separate
5. Use the instrumental stem for karaoke

#### Workflow 2: Extracting Acapellas
1. Load song in Upload tab
2. Select "Mel-RoFormer" or "Quality Ensemble"
3. Separate
4. The vocals stem is your acapella

#### Workflow 3: Creating Practice Tracks
1. Separate song (4-stem or 6-stem)
2. Load stems in Player tab
3. Mute your instrument (e.g., mute guitar)
4. Export the mix
5. Practice with the custom backing track

#### Workflow 4: Sampling and Remixing
1. Separate song (6-stem for more options)
2. Load stems in Player tab
3. Experiment with different combinations
4. Export interesting sections
5. Use in your DAW or sampler

#### Workflow 5: Recording Live Sets
1. Start recording in Recording tab
2. Play DJ set, live performance, or stream
3. Stop and save recording
4. Separate the recording
5. Extract specific stems or sections for later use

---

## Troubleshooting

### Audio Issues

**Problem**: No audio during playback in Player tab

**Solutions**:
1. Check that your Mac's audio output is not muted
2. Check master volume in the Player tab
3. Check individual stem volumes
4. Verify stems loaded correctly (all stem files are valid WAV files)
5. Restart the app and reload stems

---

**Problem**: Audio playback is crackling or distorted

**Solutions**:
1. Lower the master volume
2. Lower individual stem volumes (clipping may occur if all stems are at 100%)
3. Close other audio applications
4. Check Activity Monitor for high CPU usage
5. Restart the app

---

**Problem**: Stems are out of sync

**Solutions**:
1. This should not happen - contact support if you experience this
2. Try re-separating the file with a different model
3. Check that all stem files are the same length

---

### Separation Issues

**Problem**: "GPU out of memory" error

**Solutions**:
1. The app should automatically fall back to CPU
2. Close other applications to free up memory
3. If using ensemble mode, try a single model instead
4. Reduce chunk size in advanced settings
5. Disable GPU in settings and use CPU mode

---

**Problem**: Separation is very slow

**Solutions**:
1. **Check GPU**: Ensure GPU acceleration is enabled in settings
2. **Choose Faster Model**: Demucs v4 (4-stem) is fastest
3. **Avoid Ensemble**: Ensemble modes are intentionally slower for quality
4. **Close Other Apps**: Free up CPU/GPU resources
5. **Process Overnight**: Queue multiple files and let them process

---

**Problem**: Poor separation quality (vocals bleeding, artifacts)

**Solutions**:
1. **Try Different Model**: Each model has strengths
2. **Use Ensemble Mode**: Significantly better quality
3. **Check Source Quality**: Low-quality input = low-quality output
4. **Try Ultra Preset**: In quality settings
5. **Some songs are harder**: Dense mixes and old recordings are challenging

---

**Problem**: Model download fails

**Solutions**:
1. Check internet connection
2. Restart the app and try again
3. Check available disk space (~1.5 GB needed for all models)
4. Try downloading manually:
   ```bash
   python -c "from core.model_manager import get_model_manager; get_model_manager().download_model('mel-roformer')"
   ```

---

### Recording Issues

**Problem**: "No recording backend available"

**Solutions** (macOS 13+):
1. Grant Screen Recording permission in System Settings
2. System Settings → Privacy & Security → Screen Recording
3. Enable Stem Separator
4. Restart the app

**Solutions** (macOS 12 and earlier):
1. Install BlackHole: `brew install blackhole-2ch`
2. Select "BlackHole 2ch" in recording device dropdown
3. Configure Audio MIDI Setup as described in Recording section

---

**Problem**: Recording is silent (no audio captured)

**Solutions** (macOS 13+):
1. Verify Screen Recording permission is granted
2. Ensure audio is actually playing during recording
3. Check system volume is not muted
4. Restart the app and try again

**Solutions** (macOS 12 and earlier):
1. Verify BlackHole is installed
2. Check Multi-Output Device setup in Audio MIDI Setup
3. Ensure system audio output is set to Multi-Output Device
4. Restart the app

---

**Problem**: I can't hear audio while recording (macOS 12 and earlier)

**Solutions**:
1. Create Multi-Output Device in Audio MIDI Setup
2. Add both your speakers/headphones and BlackHole 2ch
3. Set Multi-Output Device as system audio output
4. Now audio plays through speakers AND records through BlackHole

---

### General Issues

**Problem**: App crashes or freezes

**Solutions**:
1. Check logs: `logs/app.log`
2. Look for error messages
3. Try disabling GPU in settings
4. Reduce quality preset to "Standard"
5. Process shorter files first
6. If persistent, create a GitHub issue with log excerpts

---

**Problem**: Files are very large (stems take up too much space)

**Explanation**: Stems are saved as uncompressed WAV files for quality

**Solutions**:
1. Export to MP3 after mixing to save space
2. Delete intermediate files (logs, cache) in temp/ directory
3. Only keep final mixed exports
4. Use external drive for stem storage

---

### Getting Help

If you encounter issues not covered here:

1. **Check Logs**: `logs/app.log` contains detailed error messages
2. **Enable Debug Mode**: Set `LOG_LEVEL = "DEBUG"` in `config.py`
3. **GitHub Issues**: [Create an issue](https://github.com/MaurizioFratello/StemSeparator/issues) with:
   - Clear description of the problem
   - Steps to reproduce
   - Relevant log excerpts
   - System information (macOS version, hardware)

---

## Keyboard Shortcuts Reference

| Shortcut | Action |
|----------|--------|
| ⌘ O | Open file |
| ⌘ , | Open settings |
| ⌘ Q | Quit application |
| Space | Play/Pause |
| Escape | Stop playback |
| ⌘ E | Export mixed audio |
| M | Mute selected stem |
| S | Solo selected stem |

---

## Glossary

**Stem**: An isolated component of a music track (e.g., vocals, drums)

**Separation**: The process of splitting a mixed audio file into individual stems

**Ensemble Mode**: Using multiple AI models together for superior quality

**Acapella**: Vocal stem only, without any instrumental

**Karaoke Track**: Instrumental only, without vocals

**GPU Acceleration**: Using graphics card for faster processing (Apple Silicon MPS or NVIDIA CUDA)

**Sample Rate**: Audio resolution in samples per second (44.1kHz = CD quality)

**Bit Depth**: Audio dynamic range resolution (16-bit = standard, 24-bit = professional)

**Chunking**: Splitting large files into smaller segments for processing

**Solo**: Hear only one stem while muting all others

**Mute**: Silence a specific stem

---

<div align="center">

**Happy Separating!**

For more information, visit: [https://github.com/MaurizioFratello/StemSeparator](https://github.com/MaurizioFratello/StemSeparator)

</div>
