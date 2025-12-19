# Third-Party Licenses

This document lists all third-party libraries used by Stem Separator and their respective licenses.

---

## License Compatibility

Stem Separator is licensed under the **MIT License**. All dependencies use licenses that are compatible with MIT and permit commercial use.

### License Compatibility Table

| License Type | Compatible with MIT | Commercial Use | Number of Dependencies |
|-------------|-------------------|----------------|----------------------|
| MIT | ✅ Yes | ✅ Yes | 8+ |
| BSD (3-Clause/2-Clause) | ✅ Yes | ✅ Yes | 6+ |
| Apache 2.0 | ✅ Yes | ✅ Yes | 1 |
| LGPL 3.0 | ✅ Yes (dynamic linking) | ✅ Yes | 1 |
| ISC | ✅ Yes | ✅ Yes | 1 |

**Note**: All licenses allow commercial use and distribution with proper attribution.

---

## Core Dependencies

### GUI Framework

#### PySide6 (Qt for Python)

**License**: LGPL 3.0

**Copyright**: The Qt Company Ltd.

**Usage**: Main GUI framework for the application

**Compliance Notes**:
- Stem Separator uses PySide6 via dynamic linking (not static)
- No modifications to PySide6 source code
- LGPL compliance: Users can replace PySide6 library without recompiling
- Full LGPL compliance for end-user applications

**Source**: https://pypi.org/project/PySide6/

**License Text**: https://www.gnu.org/licenses/lgpl-3.0.html

---

### Audio Separation

#### audio-separator

**License**: MIT License

**Copyright**: beveradb (Andrew Beveridge)

**Purpose**: Python wrapper for AI-powered music source separation

**Description**: Provides unified interface to multiple separation models (Demucs, MDX-Net, VR Architecture)

**Source**: https://github.com/karaokenerds/python-audio-separator

---

### Machine Learning

#### PyTorch

**License**: BSD 3-Clause License

**Copyright**: Facebook, Inc. and its affiliates (Meta)

**Purpose**: Deep learning framework for AI model inference

**Source**: https://github.com/pytorch/pytorch

**License Text**:
```
BSD 3-Clause License

Copyright (c) 2016-2025 Facebook, Inc. (Meta Platforms)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.
```

---

#### torchaudio

**License**: BSD 2-Clause License

**Copyright**: Facebook, Inc. and its affiliates (Meta)

**Purpose**: Audio processing and I/O for PyTorch

**Source**: https://github.com/pytorch/audio

---

#### ONNX Runtime

**License**: MIT License

**Copyright**: Microsoft Corporation

**Purpose**: High-performance inference engine

**Source**: https://github.com/microsoft/onnxruntime

---

### Audio Processing

#### NumPy

**License**: BSD 3-Clause License

**Copyright**: NumPy Developers

**Purpose**: Numerical computing and array operations

**Source**: https://github.com/numpy/numpy

---

#### SciPy

**License**: BSD 3-Clause License

**Copyright**: SciPy Developers

**Purpose**: Scientific computing (resampling, signal processing)

**Source**: https://github.com/scipy/scipy

---

#### soundfile

**License**: BSD 3-Clause License

**Copyright**: Bastian Bechtold

**Purpose**: Audio file reading and writing (libsndfile wrapper)

**Source**: https://github.com/bastibe/python-soundfile

---

#### librosa

**License**: ISC License

**Copyright**: Brian McFee and librosa development team

**Purpose**: Audio analysis and feature extraction

**Description**: Beat detection, tempo analysis, spectral analysis

**Source**: https://github.com/librosa/librosa

**License Text (ISC)**:
```
ISC License

Copyright (c) 2013-2025, Brian McFee

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

---

#### pydub

**License**: MIT License

**Copyright**: James Robert

**Purpose**: Audio manipulation and format conversion

**Source**: https://github.com/jiaaro/pydub

---

#### resampy

**License**: ISC License

**Copyright**: Brian McFee

**Purpose**: Audio resampling

**Source**: https://github.com/bmcfee/resampy

---

#### pyrubberband

**License**: MIT License

**Copyright**: Brian McFee

**Purpose**: Pitch-preserving time-stretching (uses rubberband library)

**Source**: https://github.com/bmcfee/pyrubberband

**Note**: Requires rubberband library (GPL with exceptions for dynamic linking)

---

### Audio I/O

#### sounddevice

**License**: MIT License

**Copyright**: Matthias Geier

**Purpose**: Audio playback and recording (PortAudio wrapper)

**Source**: https://github.com/spatialaudio/python-sounddevice

---

#### soundcard

**License**: BSD 3-Clause License

**Copyright**: Bastian Bechtold

**Purpose**: System audio recording (macOS, Windows, Linux)

**Source**: https://github.com/bastibe/SoundCard

---

### Enhanced Features (Optional)

#### deeprhythm

**License**: MIT License

**Copyright**: deeprhythm developers

**Purpose**: Enhanced BPM detection with 95%+ accuracy

**Description**: Optional dependency, falls back to librosa if not installed

**Source**: https://github.com/SunnyCYC/deeprhythm

---

### Utilities

#### requests

**License**: Apache License 2.0

**Copyright**: Kenneth Reitz and other contributors

**Purpose**: HTTP library for model downloads

**Source**: https://github.com/psf/requests

**License Text**: https://www.apache.org/licenses/LICENSE-2.0

---

#### tqdm

**License**: MIT License and MPL 2.0 (dual licensed)

**Copyright**: tqdm developers

**Purpose**: Progress bars for long-running operations

**Source**: https://github.com/tqdm/tqdm

---

#### colorlog

**License**: MIT License

**Copyright**: Sam Clements

**Purpose**: Colored terminal logging

**Source**: https://github.com/borntyping/python-colorlog

---

#### PyYAML

**License**: MIT License

**Copyright**: Ingy döt Net, Kirill Simonov

**Purpose**: YAML configuration file parsing

**Source**: https://github.com/yaml/pyyaml

---

#### psutil

**License**: BSD 3-Clause License

**Copyright**: Jay Loden, Dave Daeschler, Giampaolo Rodola

**Purpose**: System and process monitoring (CPU, memory usage)

**Source**: https://github.com/giampaolo/psutil

---

## Development and Testing Dependencies

These are used during development and are NOT included in end-user distributions:

#### pytest

**License**: MIT License

**Purpose**: Testing framework

**Source**: https://github.com/pytest-dev/pytest

---

#### pytest-qt

**License**: MIT License

**Purpose**: Qt testing support for pytest

**Source**: https://github.com/pytest-dev/pytest-qt

---

#### pytest-cov

**License**: MIT License

**Purpose**: Code coverage reporting

**Source**: https://github.com/pytest-dev/pytest-cov

---

#### pytest-mock

**License**: MIT License

**Purpose**: Mocking support for pytest

**Source**: https://github.com/pytest-dev/pytest-mock

---

#### black

**License**: MIT License

**Purpose**: Code formatter

**Source**: https://github.com/psf/black

---

#### flake8

**License**: MIT License

**Purpose**: Code linting

**Source**: https://github.com/PyCQA/flake8

---

## System Libraries and Native Dependencies

The following native libraries may be required depending on the platform:

### libsndfile

**License**: LGPL 2.1 or LGPL 3.0

**Purpose**: Audio file I/O (used by soundfile)

**Compliance**: Dynamically linked, not statically linked

**Source**: http://www.mega-nerd.com/libsndfile/

---

### PortAudio

**License**: MIT License

**Purpose**: Cross-platform audio I/O (used by sounddevice)

**Source**: http://www.portaudio.com/

---

### FFmpeg (Optional)

**License**: LGPL 2.1+ or GPL 2+ (depending on build configuration)

**Purpose**: Audio format conversion (used by pydub, optional)

**Compliance**: Executed as external process, not linked

**Note**: FFmpeg is optional and only needed for certain audio formats

**Source**: https://ffmpeg.org/

---

### Rubberband Library

**License**: GPL 2+ with commercial licensing exception for dynamic linking

**Purpose**: Time-stretching (used by pyrubberband)

**Compliance**: Dynamically linked, not statically linked

**Source**: https://breakfastquay.com/rubberband/

---

## macOS-Specific Dependencies

### ScreenCaptureKit (macOS 13+)

**License**: Apple Software License

**Purpose**: Native system audio recording on macOS 13+

**Compliance**: Uses public macOS APIs, no additional licensing required

**Source**: Apple macOS SDK

---

### BlackHole (macOS 12 and earlier)

**License**: GPL 3.0

**Copyright**: Existential Audio Inc.

**Purpose**: Virtual audio device for system audio recording (fallback)

**Compliance**: Installed as separate system driver, not distributed with app

**Note**: Users install BlackHole separately; not bundled with Stem Separator

**Source**: https://github.com/ExistentialAudio/BlackHole

---

## License Summary for Distribution

When distributing Stem Separator, the following licenses apply:

### For Binary Distributions (DMG/App)

All runtime dependencies are included. The combined work is compatible with MIT:

- **Core Application**: MIT
- **Python Runtime**: PSF License (permissive)
- **Most Dependencies**: MIT, BSD, ISC (all permissive)
- **PySide6**: LGPL 3.0 (dynamically linked, compliant)
- **Native Libraries**: Dynamically linked (LGPL compliant)

### For Source Code Distribution

Source code includes only the Stem Separator application code (MIT). Dependencies are installed separately by users via pip/conda.

---

## Attribution Requirements

When using Stem Separator, the following attribution is recommended:

```
Stem Separator uses the following open-source libraries:

- PySide6 (LGPL 3.0) - The Qt Company Ltd.
- PyTorch (BSD 3-Clause) - Facebook, Inc. (Meta)
- audio-separator (MIT) - beveradb
- librosa (ISC) - Brian McFee and librosa development team
- sounddevice (MIT) - Matthias Geier
- And many others (see THIRD_PARTY_LICENSES.md for full list)
```

---

## Verifying Licenses

To verify the exact license of any installed package:

```bash
# Activate your conda/venv environment
conda activate stem-separator

# Check license for a specific package
pip show <package-name> | grep License

# Example:
pip show PySide6 | grep License
pip show torch | grep License
```

For a full list of installed packages and their licenses:

```bash
pip-licenses --format=markdown --with-urls
```

(Requires `pip-licenses` package: `pip install pip-licenses`)

---

## Important Notes

### LGPL Compliance (PySide6)

Stem Separator complies with LGPL 3.0 requirements for PySide6:

1. **Dynamic Linking**: PySide6 is dynamically linked, not statically compiled
2. **Source Availability**: PySide6 source code is available from The Qt Company
3. **Replacement**: Users can replace PySide6 without recompiling Stem Separator
4. **No Modifications**: Stem Separator does not modify PySide6 source code

### GPL Components (Optional)

Some optional components use GPL licenses:

- **BlackHole**: GPL 3.0 (not bundled, user-installed separately)
- **FFmpeg**: GPL/LGPL (executed as external process, not linked)
- **Rubberband**: GPL 2+ (dynamically linked, exception for proprietary use)

These GPL components do not affect Stem Separator's MIT license due to:
- Dynamic linking (not static compilation)
- External process execution (not library linking)
- Optional dependencies (not required for core functionality)

---

## Updates and Changes

This document reflects the licenses as of **January 2025**.

Library licenses may change over time. For the most current information:

1. Check the official repository for each dependency
2. Use `pip show <package>` to verify installed versions
3. Consult package documentation on PyPI

---

## Contact

For questions about third-party licensing:

- Open an issue: https://github.com/MaurizioFratello/StemSeparator/issues
- Refer to individual project licenses linked above

---

## Related Documents

- [Stem Separator License (MIT)](LICENSE)
- [AI Model Licenses](docs/MODEL_LICENSES.md)
- [Contributing Guidelines](CONTRIBUTING.md)

---

**Last Updated**: January 2025

**Maintained by**: StemSeparator Project
