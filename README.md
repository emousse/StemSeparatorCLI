# Stem Separator

KI-gestützte Audio Stem Separation mit modernsten Open-Source-Modellen.

**Status**: ✅ **v1.0.0-rc1 - Produktionsreif!** (Stand: 9. November 2025)

## Features

- **Audio-Datei Upload**: Drag & Drop oder Datei-Browser
- **System Audio Recording**: Aufnahme von System-Audio (macOS mit BlackHole)
- **Multiple Stem-Konfigurationen**:
  - 4-Stem: Vocals, Drums, Bass, Other
  - 6-Stem: Vocals, Drums, Bass, Piano, Guitar, Other
- **State-of-the-Art Modelle**:
  - BS-RoFormer (beste Qualität)
  - Demucs v4 (balanced)
- **Intelligente Verarbeitung**:
  - Automatisches Chunking für große Dateien (5min Chunks)
  - GPU-Beschleunigung (MPS für Apple Silicon)
  - Automatischer Fallback auf CPU bei Problemen
  - Retry-Logik mit verschiedenen Strategien
- **Stem Player**: Abspielen und Mixen von Stems
- **Queue-System**: Mehrere Dateien nacheinander verarbeiten
- **Mehrsprachig**: Deutsch/Englisch

## Systemanforderungen

- macOS (Apple Silicon empfohlen für GPU-Beschleunigung)
- Python 3.9+
- 8 GB RAM (16 GB empfohlen)
- ~1.5 GB Speicherplatz für Modelle

### Für System Audio Recording (optional):
- BlackHole (virtuelles Audio-Device)
- Wird automatisch installiert wenn nicht vorhanden

## Installation

### 1. Repository klonen

```bash
cd /Users/moritzbruder/Documents/04_Python/StemSeparator
```

### 2. Conda Environment erstellen

```bash
# Environment aus environment.yml erstellen
conda env create -f environment.yml

# Environment aktivieren
conda activate stem-separator
```

**Alternative: Manuelle Installation mit Conda**
```bash
# Environment erstellen
conda create -n stem-separator python=3.11

# Environment aktivieren
conda activate stem-separator

# Dependencies installieren
pip install -r requirements.txt
```

### 4. Modelle vorbereiten (optional)

Die Modelle werden automatisch beim ersten Gebrauch heruntergeladen.
Für manuelles Pre-Download:

```bash
python -c "from core.model_manager import get_model_manager; get_model_manager().download_all_models()"
```

## Verwendung

### App starten

```bash
python main.py
```

### Tests ausführen

```bash
# Alle Tests
pytest

# Mit Coverage-Report
pytest --cov

# Nur Unit Tests
pytest -m unit

# Nur bestimmte Tests
pytest tests/test_logger.py
```

## Projektstruktur

```
StemSeparator/
├── main.py                 # Entry point
├── config.py               # Zentrale Konfiguration
├── requirements.txt        # Dependencies
│
├── ui/                     # GUI Components (PySide6)
│   ├── main_window.py
│   ├── file_upload_widget.py
│   ├── recording_widget.py
│   ├── queue_widget.py
│   ├── stem_player_widget.py
│   └── ...
│
├── core/                   # Business Logic
│   ├── separator.py        # Stem Separation
│   ├── recorder.py         # System Audio Recording
│   ├── audio_player.py     # Stem Player
│   ├── queue_manager.py    # Task Queue
│   ├── model_manager.py    # Model Management
│   ├── chunk_processor.py  # Audio Chunking
│   └── blackhole_installer.py
│
├── utils/                  # Utilities
│   ├── logger.py           # Logging System
│   ├── error_handler.py    # Error Handling & Retry
│   ├── i18n.py             # Internationalization
│   └── file_manager.py
│
├── tests/                  # Unit & Integration Tests
│   ├── test_logger.py
│   ├── test_error_handler.py
│   └── ...
│
└── resources/             # Resources
    ├── translations/      # DE/EN Übersetzungen
    ├── icons/            # UI Icons
    └── models/           # Downloaded Models
```

## Konfiguration

Die Hauptkonfiguration befindet sich in `config.py`:

- **Chunk-Größe**: `CHUNK_LENGTH_SECONDS = 300` (5 Minuten)
- **Standard-Modell**: `DEFAULT_MODEL = 'demucs_6s'`
- **GPU-Nutzung**: `USE_GPU = True`
- **Log-Level**: `LOG_LEVEL = "INFO"`
- **Standard-Sprache**: `DEFAULT_LANGUAGE = "de"`

## Verwendete Modelle

### BS-RoFormer
- **Größe**: ~300 MB
- **Stems**: 4 (Vocals, Drums, Bass, Other)
- **Qualität**: Beste verfügbare Qualität
- **Geschwindigkeit**: Langsamer
- **Status**: SDX23 Challenge Gewinner

### Demucs v4 (htdemucs_6s)
- **Größe**: ~240 MB
- **Stems**: 6 (Vocals, Drums, Bass, Piano, Guitar, Other)
- **Qualität**: Sehr gut
- **Geschwindigkeit**: Balanced
- **Status**: Sony MDX Challenge Gewinner

## Bekannte Limitierungen

- System Audio Recording nur auf macOS (erfordert BlackHole)
- Sehr große Dateien (>30min) werden automatisch in Chunks zerlegt
- GPU-Verarbeitung erfordert Apple Silicon Mac (MPS) oder NVIDIA GPU (CUDA)
- Erste Verarbeitung langsamer (Model Loading)

## Troubleshooting

### "BlackHole not installed"
```bash
brew install blackhole-2ch
```

### "GPU out of memory"
Die App wechselt automatisch zu CPU-Modus. Alternativ:
- Kleinere Audio-Dateien verwenden
- Andere Anwendungen schließen

### "Model download failed"
Manueller Download:
```bash
python -c "from core.model_manager import get_model_manager; get_model_manager().download_model('demucs_6s')"
```

## Logs

Logs werden gespeichert in `logs/app.log` mit automatischer Rotation.

## Entwicklung

### Code-Style
```bash
black .
flake8 .
```

### Tests hinzufügen
Neue Tests in `tests/` Verzeichnis erstellen mit Präfix `test_`.

### Neue Übersetzungen
Keys in `resources/translations/de.json` und `en.json` hinzufügen.

## Lizenz

Dieses Projekt verwendet Open-Source-Modelle:
- BS-RoFormer: [Lizenz Info]
- Demucs: MIT License

## Credits

- **audio-separator**: Python-Bibliothek für Stem Separation
- **Demucs**: Facebook Research
- **BS-RoFormer**: ByteDance AI Lab
- **PySide6**: Qt for Python
- **BlackHole**: Existential Audio Inc.

## Support

Bei Problemen:
1. Logs in `logs/app.log` prüfen
2. Issue auf GitHub erstellen
3. Debugging mit `LOG_LEVEL = "DEBUG"` in config.py

## Roadmap

- [ ] Windows/Linux Support für System Audio Recording
- [ ] Weitere Modelle (MDX-Net, etc.)
- [ ] Batch-Export-Funktionalität
- [ ] Real-time Preview während Verarbeitung
- [ ] Custom Model Training
- [ ] VST/AU Plugin Version

---

**Version**: 1.0.0
**Entwickelt mit**: Python, PySide6, PyTorch, audio-separator
