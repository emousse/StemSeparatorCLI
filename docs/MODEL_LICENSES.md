# AI Model Licenses

This document provides detailed licensing information for all AI models used in Stem Separator.

---

## Overview

Stem Separator uses state-of-the-art open-source AI models for music source separation. All models are used under permissive open-source licenses that allow both commercial and non-commercial use.

---

## Models and Their Licenses

### 1. Mel-Band RoFormer

**Purpose**: Vocal separation (recommended for best vocal quality)

**License**: MIT License

**Copyright**: Implementation by Phil Wang (lucidrains)

**Details**:
- The [Mel-Band RoFormer implementation](https://github.com/lucidrains/BS-RoFormer) is licensed under MIT
- Research paper: ["Mel-Band RoFormer for Music Source Separation"](https://arxiv.org/abs/2310.01809) (arXiv, 2023)
- Developed by ByteDance AI Labs researchers
- Mel-band scheme maps frequency bins into overlapped subbands according to the mel scale
- ~100 MB model size

**License Text Summary**:
> MIT License - Permits commercial and non-commercial use, modification, distribution, with attribution

**Sources**:
- [BS-RoFormer GitHub Repository](https://github.com/lucidrains/BS-RoFormer)
- [MIT License](https://github.com/lucidrains/BS-RoFormer/blob/main/LICENSE)

---

### 2. BS-RoFormer (Band-Split RoFormer)

**Purpose**: All-around excellent quality for all stems

**License**: MIT License (implementation), CC BY 4.0 (research paper)

**Copyright**:
- Implementation: Phil Wang (lucidrains)
- Research: ByteDance AI Labs

**Details**:
- [BS-RoFormer implementation](https://github.com/lucidrains/BS-RoFormer) is licensed under MIT
- Winner of Sound Demixing Challenge (SDX23) MSS track
- Research paper: ["Music Source Separation with Band-Split RoPE Transformer"](https://arxiv.org/abs/2309.02612)
- Achieved state-of-the-art results: 9.80 dB average SDR on MUSDB18HQ
- ~300 MB model size

**License Text Summary**:
> - **MIT License** (code): Permits commercial and non-commercial use, modification, distribution, with attribution
> - **CC BY 4.0** (paper): Allows sharing and adaptation with attribution

**Sources**:
- [BS-RoFormer GitHub Repository](https://github.com/lucidrains/BS-RoFormer)
- [MIT License](https://github.com/lucidrains/BS-RoFormer/blob/main/LICENSE)
- [Research Paper (arXiv)](https://arxiv.org/abs/2309.02612)
- [SDX23 Workshop Paper](https://sdx-workshop.github.io/papers/Wang.pdf)

---

### 3. Demucs v4 (Hybrid Transformer)

**Purpose**: 6-stem separation (vocals, drums, bass, piano, guitar, other)

**License**: MIT License

**Copyright**: Facebook, Inc. and its affiliates (Meta AI)

**Details**:
- [Official Demucs repository](https://github.com/facebookresearch/demucs) licensed under MIT
- Hybrid Transformer Demucs (v4) released December 2022
- Winner of Sony Music Demixing Challenge (MDX)
- Combines spectrogram and waveform approaches
- 4-stem model: ~160 MB
- 6-stem model: ~240 MB

**License Text Summary**:
> MIT License - Copyright (c) Facebook, Inc. and its affiliates. Permits commercial and non-commercial use, modification, distribution, with attribution

**Sources**:
- [Demucs GitHub Repository](https://github.com/facebookresearch/demucs)
- [Demucs on Hugging Face](https://huggingface.co/spaces/abidlabs/music-separation)

---

### 4. MDX-Net

**Purpose**: Vocals and instrumental separation (spectrogram CNN approach)

**License**: Varies by implementation (all open-source)

**Copyright**: KUIELab and other research teams

**Details**:
- Multiple implementations exist from Music Demixing Challenge participants
- [KUIELab-MDX-Net paper](https://arxiv.org/abs/2111.12203) licensed under CC BY 4.0
- Challenge requirement: All submissions must use open-source licenses
- Common implementations use MIT License
- Two-stream neural network architecture
- ~110-120 MB model size

**License Text Summary**:
> - **CC BY 4.0** (research paper): Allows sharing and adaptation with attribution
> - **Varies** (implementations): Must be open-source per challenge rules, commonly MIT

**Sources**:
- [KUIELab-MDX-Net Paper](https://arxiv.org/abs/2111.12203)
- [Music Demixing Challenge](https://www.aicrowd.com/challenges/music-demixing-challenge-ismir-2021)
- [Example Implementation (MIT)](https://github.com/yoyololicon/music-demixing-challenge-ismir-2021-entry)

---

## Model Distribution

### How Models Are Obtained

Models are automatically downloaded from their respective sources on first use:

1. **Model Hosting**: Models are typically hosted on:
   - Hugging Face Model Hub
   - GitHub Releases
   - Research institution servers

2. **Download Library**: Stem Separator uses the `audio-separator` library which handles:
   - Automatic model downloads
   - Model caching in `~/.cache/` or `resources/models/`
   - Checksum verification

3. **No Model Bundling**: Models are NOT included in the Stem Separator distribution to:
   - Reduce application download size
   - Ensure users always get the latest model versions
   - Respect model license requirements

---

## Ensemble Mode

When using Ensemble Mode, multiple models are combined:

- **Balanced Ensemble**: Mel-RoFormer + MDX + Demucs
- **Quality Ensemble**: Mel-RoFormer + MDX + Demucs + BS-RoFormer
- **Ultra Ensemble**: All available models

**License Compliance**: All ensemble combinations use only MIT-licensed implementations, ensuring full compatibility with Stem Separator's MIT license.

---

## License Compatibility

### Stem Separator License

Stem Separator is licensed under the **MIT License**.

### Model License Compatibility

All models used are compatible with MIT:

| Model | License | Compatible with MIT | Commercial Use |
|-------|---------|-------------------|----------------|
| Mel-Band RoFormer | MIT | ✅ Yes | ✅ Yes |
| BS-RoFormer | MIT | ✅ Yes | ✅ Yes |
| Demucs v4 | MIT | ✅ Yes | ✅ Yes |
| MDX-Net (implementations) | MIT / Open Source | ✅ Yes | ✅ Yes |

**Note**: Research papers use CC BY 4.0, which applies to the academic work, not the software implementations.

---

## Attribution Requirements

When using Stem Separator with these models, proper attribution should include:

### Recommended Citation

```
This application uses the following AI models for music source separation:

1. Mel-Band RoFormer (ByteDance AI Labs)
   Implementation by Phil Wang (lucidrains)

2. BS-RoFormer (ByteDance AI Labs)
   Winner of Sound Demixing Challenge (SDX23)
   Implementation by Phil Wang (lucidrains)

3. Demucs v4 (Meta AI / Facebook Research)
   Hybrid Transformer for Music Source Separation

4. MDX-Net (KUIELab and others)
   Music Demixing Challenge models
```

### Academic Citations

If using Stem Separator for research, please cite the relevant papers:

**Mel-Band RoFormer**:
```bibtex
@article{huang2023melband,
  title={Mel-Band RoFormer for Music Source Separation},
  author={Huang, Xuanjun and others},
  journal={arXiv preprint arXiv:2310.01809},
  year={2023}
}
```

**BS-RoFormer**:
```bibtex
@article{wang2023music,
  title={Music Source Separation with Band-Split RoPE Transformer},
  author={Wang, Wei-Tsung and others},
  journal={arXiv preprint arXiv:2309.02612},
  year={2023}
}
```

**Demucs**:
```bibtex
@inproceedings{defossez2021hybrid,
  title={Hybrid Spectrogram and Waveform Source Separation},
  author={D{\'e}fossez, Alexandre},
  booktitle={Proceedings of the ISMIR 2021 Workshop on Music Source Separation},
  year={2021}
}
```

**MDX-Net**:
```bibtex
@article{kim2021kuielab,
  title={KUIELab-MDX-Net: A Two-Stream Neural Network for Music Demixing},
  author={Kim, Minseok and others},
  journal={arXiv preprint arXiv:2111.12203},
  year={2021}
}
```

---

## Disclaimer

The model licenses and information provided in this document are accurate as of January 2025. License terms may change over time. For the most current license information, please refer to the official repositories and papers linked above.

Stem Separator developers are not responsible for model licensing changes or third-party implementations. Users are responsible for ensuring compliance with all applicable licenses when using Stem Separator commercially or in derivative works.

---

## Additional Resources

- [Stem Separator Main License (MIT)](../LICENSE)
- [Third-Party Dependencies Licenses](../THIRD_PARTY_LICENSES.md)
- [audio-separator Library](https://github.com/karaokenerds/python-audio-separator)

---

**Last Updated**: January 2025

**Maintained by**: StemSeparator Project

For questions about model licensing, please open an issue on our [GitHub repository](https://github.com/MaurizioFratello/StemSeparator/issues).
