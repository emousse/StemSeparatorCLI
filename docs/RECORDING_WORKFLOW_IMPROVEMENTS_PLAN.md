# Implementierungsplan: Recording Workflow Verbesserungen

**Datum**: 18. Dezember 2024  
**Version**: 1.0  
**Status**: Planungsphase

---

## Übersicht

Dieses Dokument beschreibt den detaillierten Implementierungsplan für 4 UX-Verbesserungen im Recording Workflow:

1. **Recording Preview**: Echtzeit-Waveform während der Aufnahme
2. **Auto-trim Silence**: Option zum automatischen Entfernen von Stille
3. **Recording Templates**: Presets für gängige Aufnahmeszenarien
4. **Post-recording Actions**: Schnellaktionen nach der Aufnahme

---

## 1. Recording Preview (Echtzeit-Waveform)

### 1.1 Technische Anforderungen

**Ziel**: Anzeige einer Echtzeit-Waveform während der Aufnahme, die sich kontinuierlich aktualisiert.

**Funktionale Anforderungen**:
- Waveform wird während der Aufnahme in Echtzeit aktualisiert
- Anzeige der letzten N Sekunden (z.B. 10-30 Sekunden) als "Rolling Window"
- Visuelle Darstellung ähnlich dem bestehenden `WaveformWidget`, aber mit dynamischen Updates
- Performance: Updates sollten flüssig sein (mindestens 10-20 FPS)
- Speicher-Effizienz: Nur relevante Daten im Speicher halten

**Nicht-funktionale Anforderungen**:
- CPU-Last: < 5% zusätzliche Last während Aufnahme
- Speicher: < 50 MB zusätzlicher Speicher für Waveform-Daten
- Latenz: < 100ms Verzögerung zwischen Audio und Visualisierung

### 1.2 Notwendige Komponenten/Bibliotheken

**Bestehende Komponenten**:
- `WaveformDisplay` (ui/widgets/waveform_widget.py) - Basis für statische Waveforms
- `Recorder` (core/recorder.py) - Bereits sammelt Audio-Chunks in `recorded_chunks`
- `RecordingWidget` (ui/widgets/recording_widget.py) - GUI-Container

**Neue Komponenten**:
- `RealtimeWaveformDisplay` - Neue Widget-Klasse für Echtzeit-Updates
- Ring-Buffer für Audio-Daten (numpy-basiert)
- Waveform-Downsampling-Logik (für Performance)

**Bibliotheken**:
- Keine neuen Dependencies erforderlich
- Nutzt bestehende: `numpy`, `PySide6`, `soundfile`

### 1.3 Implementierungsschritte

#### Schritt 1.1: Ring-Buffer für Audio-Daten
**Datei**: `core/recorder.py` (Erweiterung)

```python
# Neue Klasse in recorder.py
class AudioRingBuffer:
    """Ring buffer für Echtzeit-Waveform-Daten"""
    def __init__(self, max_duration_seconds: float, sample_rate: int, channels: int):
        # Implementierung: numpy-Array mit fester Größe
        # Circular buffer für effiziente Updates
```

**Aufwand**: 2-3 Stunden

#### Schritt 1.2: Callback-Mechanismus erweitern
**Datei**: `core/recorder.py`

- Erweitere `_record_loop()` um Callback für Audio-Chunks
- Neue Methode: `get_recent_audio_chunks(duration_seconds: float) -> np.ndarray`
- Thread-safe Zugriff auf Ring-Buffer

**Aufwand**: 2-3 Stunden

#### Schritt 1.3: RealtimeWaveformDisplay Widget
**Datei**: `ui/widgets/realtime_waveform_widget.py` (NEU)

```python
class RealtimeWaveformDisplay(QWidget):
    """Echtzeit-Waveform mit Rolling-Window-Darstellung"""
    def __init__(self, parent=None):
        # Ähnlich WaveformDisplay, aber:
        # - Kein Caching (zu teuer bei Updates)
        # - Rolling window (nur letzte N Sekunden)
        # - Optimiertes Rendering (Downsampling)
    
    def update_audio_data(self, audio_chunk: np.ndarray, sample_rate: int):
        """Update mit neuem Audio-Chunk"""
        # Append to internal buffer
        # Downsample für Display
        # Trigger repaint
```

**Aufwand**: 6-8 Stunden

#### Schritt 1.4: Integration in RecordingWidget
**Datei**: `ui/widgets/recording_widget.py`

- Ersetze oder ergänze Level-Meter mit `RealtimeWaveformDisplay`
- Connect zu Recorder-Callback für Audio-Chunks
- Update-Logik: QTimer mit 50-100ms Intervall
- Toggle-Option: "Show Waveform" Checkbox

**Aufwand**: 4-5 Stunden

#### Schritt 1.5: Performance-Optimierungen
- Downsampling: Nur jeden N-ten Sample für Display verwenden
- Lazy Rendering: Nur bei sichtbaren Änderungen neuzeichnen
- Memory Management: Alte Daten automatisch verwerfen

**Aufwand**: 3-4 Stunden

### 1.4 Aufwandseinschätzung

| Phase | Aufwand | Risiko |
|-------|---------|--------|
| Ring-Buffer & Callback | 4-6h | Niedrig |
| RealtimeWaveformDisplay | 6-8h | Mittel |
| Integration | 4-5h | Niedrig |
| Performance-Tuning | 3-4h | Mittel |
| Testing & Bugfixes | 4-6h | Niedrig |
| **Gesamt** | **21-29h** | **~3-4 Tage** |

**Risiken**:
- Performance-Probleme bei langen Aufnahmen (mit Ring-Buffer gelöst)
- Thread-Safety bei GUI-Updates (mit Qt Signals gelöst)

---

## 2. Auto-trim Silence (Option)

### 2.1 Technische Anforderungen

**Ziel**: Optionale automatische Entfernung von Stille am Anfang und/oder Ende der Aufnahme.

**Funktionale Anforderungen**:
- Checkbox "Auto-trim silence" in RecordingWidget
- Optionen:
  - Trim leading silence (bereits vorhanden, aber optional)
  - Trim trailing silence (NEU)
  - Threshold konfigurierbar (default: -40 dB)
  - Min. Silence-Duration konfigurierbar (default: 0.5s)
- Preview der Trim-Positionen vor dem Speichern (optional)
- Info-Anzeige: "X.Xs silence removed"

**Nicht-funktionale Anforderungen**:
- Performance: Trim-Operation sollte < 1 Sekunde für 10 Minuten Audio dauern
- Genauigkeit: Trim an Zero-Crossings (bereits implementiert)

### 2.2 Notwendige Komponenten/Bibliotheken

**Bestehende Komponenten**:
- `trim_leading_silence()` (utils/audio_processing.py) - Bereits vorhanden
- `Recorder.stop_recording()` - Ruft bereits `trim_leading_silence()` auf

**Neue Komponenten**:
- `trim_trailing_silence()` - Neue Funktion in `utils/audio_processing.py`
- `trim_both_ends()` - Wrapper-Funktion für beide Enden
- UI-Controls in `RecordingWidget`

**Bibliotheken**:
- Keine neuen Dependencies

### 2.3 Implementierungsschritte

#### Schritt 2.1: trim_trailing_silence() implementieren
**Datei**: `utils/audio_processing.py`

```python
def trim_trailing_silence(
    audio_data: np.ndarray,
    sample_rate: int,
    threshold_db: float = -40.0,
    min_silence_duration: float = 0.5,
) -> Tuple[np.ndarray, float]:
    """Remove silence from the end of audio"""
    # Ähnlich trim_leading_silence, aber rückwärts
    # Finde letztes Sample über Threshold
    # Suche Zero-Crossing
    # Trim von hinten
```

**Aufwand**: 3-4 Stunden

#### Schritt 2.2: trim_both_ends() Wrapper
**Datei**: `utils/audio_processing.py`

```python
def trim_both_ends(
    audio_data: np.ndarray,
    sample_rate: int,
    threshold_db: float = -40.0,
    min_silence_duration: float = 0.5,
    trim_leading: bool = True,
    trim_trailing: bool = False,
) -> Tuple[np.ndarray, float, float]:
    """Trim both ends with configurable options"""
    # Returns: (trimmed_audio, leading_trim_duration, trailing_trim_duration)
```

**Aufwand**: 2-3 Stunden

#### Schritt 2.3: Recorder-Integration
**Datei**: `core/recorder.py`

- Neue Parameter in `stop_recording()`:
  - `auto_trim: bool = False`
  - `trim_leading: bool = True`
  - `trim_trailing: bool = False`
  - `trim_threshold_db: float = -40.0`
- Ersetze direkten `trim_leading_silence()`-Aufruf durch `trim_both_ends()`
- Update `RecordingInfo` um `trailing_trimmed_duration`

**Aufwand**: 3-4 Stunden

#### Schritt 2.4: UI-Controls in RecordingWidget
**Datei**: `ui/widgets/recording_widget.py`

- Neue Checkbox: "Auto-trim silence"
- Sub-Optionen (nur sichtbar wenn Checkbox aktiv):
  - "Trim leading silence" (default: checked)
  - "Trim trailing silence" (default: unchecked)
- Threshold-SpinBox (optional, erweitert)
- Info-Label: Zeigt Trim-Statistik nach Aufnahme

**Aufwand**: 4-5 Stunden

#### Schritt 2.5: Settings-Persistierung
**Datei**: `ui/settings_manager.py`

- Speichere Auto-trim-Präferenzen in User-Settings
- Default-Werte: Leading=True, Trailing=False

**Aufwand**: 1-2 Stunden

### 2.4 Aufwandseinschätzung

| Phase | Aufwand | Risiko |
|-------|---------|--------|
| trim_trailing_silence() | 3-4h | Niedrig |
| trim_both_ends() Wrapper | 2-3h | Niedrig |
| Recorder-Integration | 3-4h | Niedrig |
| UI-Controls | 4-5h | Niedrig |
| Settings | 1-2h | Niedrig |
| Testing | 2-3h | Niedrig |
| **Gesamt** | **15-21h** | **~2-3 Tage** |

**Risiken**: Minimal, da `trim_leading_silence()` bereits funktioniert und als Vorlage dient.

---

## 3. Recording Templates (Presets)

### 3.1 Technische Anforderungen

**Ziel**: Vordefinierte Presets für gängige Aufnahmeszenarien mit optimierten Einstellungen.

**Funktionale Anforderungen**:
- Template-Auswahl in RecordingWidget (Dropdown)
- Templates:
  - **Podcast**: Mono, 44.1kHz, Auto-trim leading, Normalisierung
  - **Music**: Stereo, 48kHz, Kein Auto-trim, High Quality
  - **System Audio**: Stereo, 48kHz, Auto-trim leading, Standard
  - **Voice Memo**: Mono, 44.1kHz, Auto-trim both ends, Kompression
- Template-Eigenschaften:
  - Sample Rate
  - Channels (Mono/Stereo)
  - Auto-trim Settings
  - Normalisierung (optional, zukünftig)
  - Kompression (optional, zukünftig)
- Custom Template: Benutzer kann eigene Templates speichern
- Template-Persistierung in Settings

**Nicht-funktionale Anforderungen**:
- Template-Wechsel sollte sofort alle relevanten UI-Controls aktualisieren
- Templates sollten erweiterbar sein (für zukünftige Features)

### 3.2 Notwendige Komponenten/Bibliotheken

**Bestehende Komponenten**:
- `RecordingWidget` - UI-Container
- `Recorder` - Core-Logik
- `SettingsManager` - Persistierung

**Neue Komponenten**:
- `RecordingTemplate` - Dataclass für Template-Definition
- `RecordingTemplateManager` - Verwaltung von Templates
- Template-UI in `RecordingWidget`

**Bibliotheken**:
- Keine neuen Dependencies
- Nutzt bestehende: `dataclasses`, `json` (für Persistierung)

### 3.3 Implementierungsschritte

#### Schritt 3.1: RecordingTemplate Dataclass
**Datei**: `core/recorder.py` oder `config.py`

```python
@dataclass
class RecordingTemplate:
    """Recording template configuration"""
    name: str
    description: str
    sample_rate: int
    channels: int
    auto_trim_leading: bool
    auto_trim_trailing: bool
    trim_threshold_db: float
    # Future: normalize, compress, etc.
```

**Aufwand**: 1-2 Stunden

#### Schritt 3.2: Template-Definitionen
**Datei**: `config.py`

```python
RECORDING_TEMPLATES = {
    "podcast": RecordingTemplate(
        name="Podcast",
        description="Optimized for voice recordings",
        sample_rate=44100,
        channels=1,  # Mono
        auto_trim_leading=True,
        auto_trim_trailing=False,
        trim_threshold_db=-40.0,
    ),
    "music": RecordingTemplate(...),
    "system_audio": RecordingTemplate(...),
    "voice_memo": RecordingTemplate(...),
}
```

**Aufwand**: 2-3 Stunden

#### Schritt 3.3: RecordingTemplateManager
**Datei**: `core/template_manager.py` (NEU)

```python
class RecordingTemplateManager:
    """Manages recording templates and user customizations"""
    def __init__(self):
        self.default_templates = RECORDING_TEMPLATES
        self.custom_templates = {}  # Loaded from settings
    
    def get_template(self, template_id: str) -> RecordingTemplate:
        """Get template by ID"""
    
    def save_custom_template(self, template: RecordingTemplate):
        """Save user-created template"""
    
    def list_templates(self) -> List[RecordingTemplate]:
        """List all available templates"""
```

**Aufwand**: 4-5 Stunden

#### Schritt 3.4: UI-Integration in RecordingWidget
**Datei**: `ui/widgets/recording_widget.py`

- Neues Dropdown: "Recording Template" (vor Device-Selection)
- Template-Auswahl aktualisiert:
  - Sample Rate ComboBox
  - Channels ComboBox
  - Auto-trim Checkboxes
- "Customize Template" Button (öffnet Dialog für eigene Templates)
- Template-Info-Label: Zeigt Template-Beschreibung

**Aufwand**: 6-8 Stunden

#### Schritt 3.5: Recorder-Integration
**Datei**: `core/recorder.py`

- Neue Methode: `apply_template(template: RecordingTemplate)`
- Setzt Sample Rate, Channels, Auto-trim Settings
- Wird von `RecordingWidget` vor `start_recording()` aufgerufen

**Aufwand**: 2-3 Stunden

#### Schritt 3.6: Custom Template Dialog
**Datei**: `ui/dialogs/template_dialog.py` (NEU)

- Dialog zum Erstellen/Bearbeiten von Templates
- Formular mit allen Template-Eigenschaften
- "Save as Custom Template" Button
- Template-Liste mit Delete-Option

**Aufwand**: 5-6 Stunden

#### Schritt 3.7: Settings-Persistierung
**Datei**: `ui/settings_manager.py`

- Speichere Custom Templates in `user_settings.json`
- Load Templates beim App-Start
- Default Template-Präferenz speichern

**Aufwand**: 2-3 Stunden

### 3.4 Aufwandseinschätzung

| Phase | Aufwand | Risiko |
|-------|---------|--------|
| Dataclass & Definitions | 3-5h | Niedrig |
| TemplateManager | 4-5h | Niedrig |
| UI-Integration | 6-8h | Mittel |
| Recorder-Integration | 2-3h | Niedrig |
| Custom Template Dialog | 5-6h | Mittel |
| Settings | 2-3h | Niedrig |
| Testing | 3-4h | Niedrig |
| **Gesamt** | **25-34h** | **~3-4 Tage** |

**Risiken**:
- UI-Komplexität bei vielen Optionen (mit klarer Struktur gelöst)
- Template-Kompatibilität bei zukünftigen Features (mit Versionierung gelöst)

---

## 4. Post-recording Actions (Schnellaktionen)

### 4.1 Technische Anforderungen

**Ziel**: Schnellaktionen direkt nach dem Speichern einer Aufnahme, ohne manuelles Navigieren.

**Funktionale Anforderungen**:
- Dialog oder Button-Bar nach erfolgreicher Aufnahme
- Aktionen:
  - **Separate Now**: Sofortige Separation starten (mit Standard-Modell)
  - **Add to Queue**: Zur Queue hinzufügen (mit aktuellen Settings)
  - **Save Only**: Nur speichern (aktuelles Verhalten)
  - **Open in Upload**: Datei in Upload-Tab öffnen (aktuelles Verhalten)
- Optionale Aktionen (erweiterbar):
  - **Load in Player**: Direkt in Player-Tab laden (wenn bereits getrennt)
  - **Export**: Direkt Export-Dialog öffnen
- Dialog sollte nicht blockierend sein (optional: "Don't show again")

**Nicht-funktionale Anforderungen**:
- Dialog sollte intuitiv und schnell bedienbar sein
- Default-Aktion sollte klar sein (z.B. "Add to Queue")
- Keyboard-Shortcuts für schnelle Auswahl (1, 2, 3, Esc)

### 4.2 Notwendige Komponenten/Bibliotheken

**Bestehende Komponenten**:
- `RecordingWidget` - Emittiert `recording_saved` Signal
- `MainWindow` - Verbindet Recording zu Upload/Queue
- `UploadWidget` - `add_file()` Methode
- `QueueWidget` - `add_task()` Methode

**Neue Komponenten**:
- `PostRecordingDialog` - Dialog für Schnellaktionen
- Oder: Button-Bar direkt in `RecordingWidget` (einfacher)

**Bibliotheken**:
- Keine neuen Dependencies

### 4.3 Implementierungsschritte

#### Schritt 4.1: PostRecordingDialog (Option A: Dialog)
**Datei**: `ui/dialogs/post_recording_dialog.py` (NEU)

```python
class PostRecordingDialog(QDialog):
    """Dialog mit Schnellaktionen nach Aufnahme"""
    # Signal: action_selected(str, Path)
    # Actions: "separate_now", "add_to_queue", "save_only", "open_upload"
    
    def __init__(self, file_path: Path, parent=None):
        # Große Buttons für jede Aktion
        # Keyboard-Shortcuts (1-4)
        # "Don't show again" Checkbox
        # File-Info anzeigen
```

**Aufwand**: 5-6 Stunden

#### Schritt 4.2: Button-Bar in RecordingWidget (Option B: Einfacher)
**Datei**: `ui/widgets/recording_widget.py`

- Neue Button-Bar nach erfolgreicher Aufnahme
- Sichtbar nur wenn `recording_saved` Signal emittiert wurde
- Buttons: "Separate Now", "Add to Queue", "Save Only"
- Auto-hide nach 10 Sekunden oder bei neuer Aufnahme

**Aufwand**: 4-5 Stunden (einfacher als Dialog)

#### Schritt 4.3: Action-Handler in MainWindow
**Datei**: `ui/main_window.py`

- Erweitere `_on_recording_saved()` um Action-Parameter
- Neue Methoden:
  - `_on_separate_now(file_path: Path)`
  - `_on_add_to_queue(file_path: Path)`
  - `_on_save_only(file_path: Path)` (aktuelles Verhalten)

**Aufwand**: 3-4 Stunden

#### Schritt 4.4: Separate Now Implementierung
**Datei**: `ui/main_window.py`

```python
def _on_separate_now(self, file_path: Path):
    """Start separation immediately with default model"""
    # Get default model from settings
    # Add to queue
    # Start queue processing
    # Switch to Queue tab
    # Show notification
```

**Aufwand**: 2-3 Stunden

#### Schritt 4.5: Settings für Default-Aktion
**Datei**: `ui/settings_manager.py`

- Neue Setting: `default_post_recording_action`
- Optionen: "separate_now", "add_to_queue", "save_only", "ask"
- Wenn "ask": Zeige Dialog/Button-Bar
- Wenn andere: Führe Aktion automatisch aus

**Aufwand**: 2-3 Stunden

#### Schritt 4.6: Keyboard-Shortcuts
**Datei**: `ui/dialogs/post_recording_dialog.py` oder `recording_widget.py`

- 1 = Separate Now
- 2 = Add to Queue
- 3 = Save Only
- Esc = Cancel/Close

**Aufwand**: 1-2 Stunden

### 4.4 Aufwandseinschätzung

| Phase | Aufwand | Risiko |
|-------|---------|--------|
| Dialog/Button-Bar | 4-6h | Niedrig |
| Action-Handler | 3-4h | Niedrig |
| Separate Now | 2-3h | Niedrig |
| Settings | 2-3h | Niedrig |
| Keyboard-Shortcuts | 1-2h | Niedrig |
| Testing | 2-3h | Niedrig |
| **Gesamt** | **14-21h** | **~2-3 Tage** |

**Risiken**: Minimal, da bestehende Infrastruktur genutzt wird.

---

## Gesamtaufwand & Priorisierung

### Aufwand nach Feature

| Feature | Aufwand | Komplexität | Priorität |
|---------|---------|-------------|-----------|
| 1. Recording Preview | 21-29h | Hoch | Mittel |
| 2. Auto-trim Silence | 15-21h | Mittel | Hoch |
| 3. Recording Templates | 25-34h | Mittel | Mittel |
| 4. Post-recording Actions | 14-21h | Niedrig | Hoch |
| **Gesamt** | **75-105h** | - | - |

### Empfohlene Implementierungsreihenfolge

1. **Phase 1 (Quick Wins)**: Post-recording Actions (14-21h)
   - Schnell umsetzbar
   - Hoher UX-Impact
   - Geringes Risiko

2. **Phase 2 (High Value)**: Auto-trim Silence (15-21h)
   - Nutzt bestehende Infrastruktur
   - Hoher UX-Impact
   - Geringes Risiko

3. **Phase 3 (Nice to Have)**: Recording Templates (25-34h)
   - Erhöht Flexibilität
   - Mittlerer UX-Impact
   - Mittleres Risiko

4. **Phase 4 (Advanced)**: Recording Preview (21-29h)
   - Technisch anspruchsvoll
   - Hoher UX-Impact, aber komplex
   - Höheres Risiko (Performance)

### Gesamtaufwand

**Optimistisch**: 75 Stunden (~10 Arbeitstage)  
**Realistisch**: 90 Stunden (~11-12 Arbeitstage)  
**Pessimistisch**: 105 Stunden (~13-14 Arbeitstage)

**Empfehlung**: Mit Phase 1 + 2 beginnen (29-42h, ~4-5 Tage), dann evaluieren.

---

## Abhängigkeiten & Voraussetzungen

### Technische Voraussetzungen
- Bestehende Recording-Infrastruktur funktioniert
- WaveformWidget als Referenz für Preview
- Settings-System für Persistierung

### Externe Abhängigkeiten
- Keine neuen Python-Packages erforderlich
- Alle benötigten Bibliotheken bereits vorhanden

### Risiken & Mitigation

| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|--------|-------------------|--------|------------|
| Performance-Probleme bei Preview | Mittel | Hoch | Ring-Buffer + Downsampling |
| Thread-Safety bei GUI-Updates | Niedrig | Hoch | Qt Signals verwenden |
| Template-Kompatibilität | Niedrig | Mittel | Versionierung in Templates |
| UI-Überlastung | Niedrig | Mittel | Optionale Features, klare Struktur |

---

## Testing-Strategie

### Unit Tests
- `trim_trailing_silence()` Funktion
- `RecordingTemplate` Dataclass
- `RecordingTemplateManager` Logik

### Integration Tests
- Recording → Auto-trim → Save Workflow
- Recording → Template → Start Workflow
- Recording → Post-Action → Queue Workflow

### UI Tests
- Recording Preview Updates korrekt
- Template-Auswahl aktualisiert UI
- Post-recording Dialog/Buttons funktionieren

### Performance Tests
- Recording Preview: CPU-Last < 5%
- Recording Preview: Speicher < 50 MB
- Auto-trim: < 1 Sekunde für 10 Minuten Audio

---

## Dokumentation

### Code-Dokumentation
- Docstrings für alle neuen Funktionen/Klassen
- Inline-Kommentare für komplexe Logik (z.B. Ring-Buffer)

### User-Dokumentation
- README-Update: Neue Recording-Features
- Tooltips in UI für alle neuen Controls
- Settings-Dokumentation für Templates

---

## Fazit

Alle 4 Features sind technisch machbar und nutzen die bestehende Architektur. Die empfohlene Reihenfolge (Post-Actions → Auto-trim → Templates → Preview) maximiert den UX-Impact bei minimalem Risiko.

**Nächste Schritte**:
1. Review dieses Plans
2. Entscheidung: Dialog vs. Button-Bar für Post-Actions
3. Start mit Phase 1 (Post-recording Actions)

