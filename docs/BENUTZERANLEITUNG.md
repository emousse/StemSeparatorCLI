# Stem Separator - Benutzeranleitung

Diese umfassende Anleitung hilft Ihnen beim Einstieg in Stem Separator und zeigt, wie Sie alle Funktionen optimal nutzen können.

---

## Inhaltsverzeichnis

1. [Erste Schritte](#erste-schritte)
2. [Übersicht Hauptfenster](#übersicht-hauptfenster)
3. [Audio-Dateien separieren](#audio-dateien-separieren)
4. [System-Audio aufnehmen](#system-audio-aufnehmen)
5. [Stems abspielen und mischen](#stems-abspielen-und-mischen)
6. [Audio exportieren](#audio-exportieren)
7. [Einstellungen](#einstellungen)
8. [Tipps und Best Practices](#tipps-und-best-practices)
9. [Fehlerbehebung](#fehlerbehebung)

---

## Erste Schritte

### Erster Start

Beim ersten Start von Stem Separator:

1. **macOS Sicherheit**: Falls eine Sicherheitswarnung erscheint, klicken Sie mit rechts auf das App-Icon und wählen Sie "Öffnen"
2. **Modell-Download**: Die App lädt automatisch KI-Modelle herunter, wenn Sie das erste Mal eine Separation durchführen (kann einige Minuten dauern)
3. **Berechtigungen**: Falls Sie die Aufnahmefunktion nutzen möchten:
   - **macOS 13+**: Gewähren Sie die "Bildschirmaufnahme"-Berechtigung
   - **macOS 12 und älter**: Die App führt Sie durch die Installation von BlackHole

### Grundlegender Workflow

Der typische Arbeitsablauf ist:
1. **Laden** von Audio (Datei-Upload oder Aufnahme)
2. **Separieren** in Stems (Vocals, Drums, Bass, etc.)
3. **Abspielen** und Mischen der Stems
4. **Exportieren** des Mix

---

## Übersicht Hauptfenster

Das Stem Separator Fenster hat vier Haupt-Tabs:

### 1. Upload-Tab
- Audio-Dateien zum Separieren laden
- KI-Modelle und Qualitätseinstellungen wählen
- Separation starten

### 2. Aufnahme-Tab
- System-Audio vom Mac aufnehmen
- Keine externen Kabel nötig
- Direkte Aufnahme von jeder Anwendung

### 3. Warteschlange-Tab
- Separations-Jobs verwalten
- Fortschritt überwachen
- Operationen abbrechen oder wiederholen

### 4. Player-Tab
- Separierte Stems laden und abspielen
- Stems mit individuellen Lautstärke-Reglern mischen
- Mixed Audio exportieren

---

## Audio-Dateien separieren

### Basis-Separation

1. **Zum Upload-Tab navigieren**
   - Klicken Sie auf den "Upload"-Tab oben im Fenster

2. **Audio-Datei laden**
   - **Drag & Drop**: Ziehen Sie eine Audio-Datei direkt ins Fenster
   - **Datei-Browser**: Klicken Sie auf "Audio-Datei auswählen" und suchen Sie Ihre Datei
   - Unterstützte Formate: WAV, MP3, FLAC, M4A, OGG, AAC

3. **Modell wählen**
   - **Mel-RoFormer** (Empfohlen): Beste Qualität für Vocals
   - **BS-RoFormer**: Exzellente Allround-Qualität
   - **Demucs v4 (6-stem)**: Separiert auch Klavier und Gitarre
   - **Demucs v4 (4-stem)**: Schneller, gute Qualität
   - **MDX-Net**: Stark für Vocals und Lead-Instrumente

4. **Separations-Modus wählen**
   - **4-Stem**: Vocals, Drums, Bass, Other
   - **6-Stem**: Vocals, Drums, Bass, Piano, Guitar, Other (nur Demucs)
   - **2-Stem (Karaoke)**: Vocals, Instrumental

5. **"Separieren" klicken**
   - Der Job erscheint im Warteschlange-Tab
   - Fortschritt wird mit einem Fortschrittsbalken angezeigt
   - Verarbeitungszeit variiert je nach Dateilänge und Modell

6. **Ihre Stems finden**
   - Stems werden gespeichert in: `temp/separated/[Dateiname]/[Modellname]/`
   - Jeder Stem ist eine separate WAV-Datei

### Ensemble-Separation (Maximale Qualität)

Für professionelle Anwendungen, bei denen Qualität entscheidend ist:

1. **"Ensemble-Modus" aktivieren** im Upload-Tab

2. **Ensemble-Konfiguration wählen**:
   - **Balanced** (~2x langsamer): Gute Balance zwischen Qualität und Geschwindigkeit
   - **Quality** (~2.5x langsamer): Professionelle Qualität (empfohlen)
   - **Ultra** (~3.5x langsamer): Maximal mögliche Qualität

3. **Funktionsweise**:
   - Ensemble-Modus nutzt mehrere KI-Modelle
   - Vocals werden zuerst mit 2-3 kombinierten Modellen verarbeitet
   - Verbleibende Stems (Drums, Bass, Other) werden dann verarbeitet
   - Ergebnisse werden für überlegene Qualität gemischt

4. **Wann verwenden**:
   - Professionelle Musikproduktion
   - Kritische Vocal-Extraktion
   - Wenn Qualität wichtiger ist als Geschwindigkeit
   - Finale Master und Releases

### Verarbeitungszeit verstehen

| Modell | Geschwindigkeit | Qualität | Am besten für |
|--------|-----------------|----------|---------------|
| Demucs v4 (4-stem) | Schnell | Gut | Schnelle Separationen |
| Mel-RoFormer | Mittel | Exzellent | Vocal-Extraktion |
| BS-RoFormer | Mittel | Exzellent | Allround-Qualität |
| Demucs v4 (6-stem) | Mittel | Sehr gut | Piano/Gitarre-Separation |
| Balanced Ensemble | Langsam (2x) | Überlegen | Professionelle Arbeit |
| Quality Ensemble | Langsamer (2.5x) | Exzellent | Kritische Anwendungen |
| Ultra Ensemble | Am langsamsten (3.5x) | Maximum | Finale Master |

**Hinweis**: Zeiten sind ungefähre Werte und hängen ab von:
- Dateilänge (längere Dateien = mehr Verarbeitung)
- Ihrer Hardware (Apple Silicon M1/M2/M3 ist am schnellsten)
- GPU-Verfügbarkeit (GPU ist viel schneller als CPU)

### Große Dateien (>30 Minuten)

Für Dateien länger als 30 Minuten:
- Die App teilt die Datei automatisch in 5-Minuten-Chunks
- Jeder Chunk wird separat verarbeitet
- Ergebnisse werden nahtlos kombiniert
- Kein Qualitätsverlust durch Chunking

---

## System-Audio aufnehmen

Stem Separator kann Audio aufnehmen, das auf Ihrem Mac abgespielt wird, ohne Kabel oder zusätzliche Hardware.

### macOS 13+ (Ventura und neuer) - Empfohlene Methode

1. **Zum Aufnahme-Tab navigieren**

2. **Bildschirmaufnahme-Berechtigung gewähren** (nur beim ersten Mal)
   - Klicken Sie auf "Aufnahme starten"
   - macOS fragt nach "Bildschirmaufnahme"-Berechtigung
   - Öffnen Sie Systemeinstellungen → Datenschutz & Sicherheit → Bildschirmaufnahme
   - Aktivieren Sie Berechtigung für Stem Separator
   - Starten Sie die App neu

3. **Aufnahme starten**
   - Klicken Sie auf "Aufnahme starten"
   - Die Aufnahme-Anzeige erscheint (rotes Icon)
   - Keine Eingabegerät-Auswahl nötig

4. **Audio abspielen**
   - Spielen Sie Musik, Videos oder beliebiges Audio auf Ihrem Mac
   - Alles System-Audio wird automatisch erfasst
   - Qualität: 44.1 kHz, Stereo, verlustfrei

5. **Stoppen und Speichern**
   - Klicken Sie auf "Stoppen & Speichern"
   - Wählen Sie Dateinamen und Speicherort
   - Die Aufnahme wird als WAV-Datei gespeichert

6. **Aufnahme separieren**
   - Die aufgenommene Datei kann sofort im Upload-Tab verwendet werden

### macOS 12 und älter - BlackHole-Methode

1. **BlackHole installieren** (nur beim ersten Mal)
   - Die App bietet an, BlackHole automatisch zu installieren
   - Oder manuell: `brew install blackhole-2ch`

2. **Zum Aufnahme-Tab navigieren**

3. **Eingabegerät wählen**
   - Im Geräte-Dropdown wählen Sie "BlackHole 2ch"

4. **macOS Audio konfigurieren** (einmalige Einrichtung)
   - Öffnen Sie "Audio-MIDI-Setup" (in Programme → Dienstprogramme)
   - Erstellen Sie ein "Multi-Output-Gerät"
   - Aktivieren Sie sowohl Ihre Lautsprecher als auch "BlackHole 2ch"
   - In Systemeinstellungen → Ton wählen Sie dieses Multi-Output-Gerät
   - Dies ermöglicht es, Audio zu hören während Sie aufnehmen

5. **Aufnahme starten**
   - Klicken Sie auf "Aufnahme starten" in Stem Separator
   - Spielen Sie Ihre Audio-Quelle ab
   - Klicken Sie auf "Stoppen & Speichern" wenn fertig

### Aufnahme-Tipps

- **Qualität**: Nehmen Sie immer in höchster Qualität auf, die in Ihrer Quelle verfügbar ist
- **Stille**: Entfernen Sie Stille am Anfang/Ende durch Trimmen der Audio-Datei
- **Lautstärke**: Halten Sie die Systemlautstärke auf einem angenehmen Level (50-80%)
- **Clipping vermeiden**: Falls die Aufnahme verzerrt ist, reduzieren Sie die Systemlautstärke
- **Hintergrundgeräusche**: Schließen Sie andere Anwendungen um CPU-Last zu reduzieren

---

## Stems abspielen und mischen

Nach der Separation nutzen Sie den Player-Tab zum Anhören und Mischen Ihrer Stems.

### Stems laden

**Methode 1: Volle Session laden**
1. Klicken Sie auf "Stems laden"
2. Navigieren Sie zu Ihrem separierte-Stems-Ordner
3. Wählen Sie eine beliebige Datei im Ordner
4. Alle Stems in diesem Ordner werden automatisch geladen

**Methode 2: Einzelne Stems laden**
1. Klicken Sie auf "Stem hinzufügen"
2. Wählen Sie einzelne Stem-Dateien
3. Wiederholen Sie dies für jeden Stem, den Sie laden möchten

### Player-Steuerung

#### Wiedergabe-Steuerung
- **Play/Pause**: Wiedergabe starten oder pausieren
- **Stop**: Wiedergabe stoppen und zum Anfang zurückkehren
- **Positions-Slider**: Ziehen um zu beliebiger Position zu springen

#### Stem-Mixer

Jeder Stem hat eigene Regler:

- **Lautstärke-Slider**: Lautstärke jedes Stems anpassen (0-100%)
- **M (Mute)**: Diesen Stem stumm schalten
- **S (Solo)**: Nur diesen Stem hören (schaltet alle anderen stumm)
- **Stem-Label**: Zeigt den Stem-Namen (Vocals, Drums, etc.)

#### Master-Regler
- **Master-Lautstärke**: Gesamt-Lautstärkeregler für alle Stems
- **Wellenform-Anzeige**: Visuelle Darstellung des Audios
- **Zeit-Anzeige**: Aktuelle Position und Gesamtdauer

### Mix-Tipps

1. **Mit allen Stems beginnen**: Laden Sie alle Stems und spielen Sie zuerst den Original-Mix
2. **Stems isolieren**: Nutzen Sie Solo (S) um jeden Stem einzeln zu hören
3. **Probleme finden**: Nutzen Sie Mute (M) um zu identifizieren, welcher Stem Probleme hat
4. **Variationen erstellen**:
   - **Karaoke**: Vocals stumm schalten
   - **Acapella**: Nur Vocals solo
   - **Instrumental-Fokus**: Vocals leiser, Drums/Bass lauter
   - **Übungs-Track**: Ihr Instrument stumm schalten zum Mitspielen

5. **Pegel balancieren**: Lautstärke-Slider so anpassen, dass kein Stem zu laut oder zu leise ist
6. **Original als Referenz**: Spielen Sie gelegentlich die Originaldatei zum Vergleich

### Tastatur-Shortcuts

- **Leertaste**: Play/Pause
- **Escape**: Stop
- **Pfeiltasten**: Position suchen
- **M**: Ausgewählten Stem muten
- **S**: Ausgewählten Stem solo

---

## Audio exportieren

### Gemischte Stems exportieren

1. **Stems laden und mischen** im Player-Tab
2. **Lautstärken anpassen** auf gewünschten Mix
3. **"Mixed exportieren" klicken**
4. **Einstellungen wählen**:
   - **Format**: WAV (verlustfrei) oder MP3 (komprimiert)
   - **Sample-Rate**: 44100 Hz (CD-Qualität) oder 48000 Hz (professionell)
   - **Bit-Tiefe** (nur WAV): 16-bit (Standard) oder 24-bit (professionell)
   - **MP3-Bitrate**: 128, 192, 256 oder 320 kbps
5. **Ausgabe-Speicherort wählen** und Dateinamen eingeben
6. **"Exportieren" klicken**

### Export-Anwendungsfälle

| Export-Format | Am besten für |
|---------------|---------------|
| WAV 16-bit 44.1kHz | CD-Master, finale Exports |
| WAV 24-bit 48kHz | Professionelle Audio-Produktion |
| MP3 320kbps | Hochwertiges Teilen, Streaming |
| MP3 192kbps | Gute Qualität, kleinere Dateigröße |
| MP3 128kbps | Web-Nutzung, Demos (nicht für Master empfohlen) |

---

## Einstellungen

### Einstellungen öffnen

- **Menüleiste**: Stem Separator → Einstellungen (⌘,)
- **Oder**: Klicken Sie auf das Einstellungs-Icon im Hauptfenster

### Verfügbare Einstellungen

#### Sprache
- **Deutsch**: Vollständige deutsche Oberfläche
- **English**: Vollständige englische Oberfläche

#### GPU-Beschleunigung
- **GPU aktivieren**: Apple Silicon (MPS) oder NVIDIA (CUDA) für schnellere Verarbeitung nutzen
- **GPU deaktivieren**: CPU-Modus erzwingen (nützlich zur Fehlerbehebung)

#### Standard-Modell
- Wählen Sie, welches KI-Modell standardmäßig ausgewählt ist

#### Qualitäts-Voreinstellung
- **Schnell**: Schnelle Separation, gute Qualität
- **Standard**: Ausgewogene Qualität und Geschwindigkeit (Standard)
- **Hoch**: Bessere Qualität, langsamer
- **Ultra**: Maximale Qualität, am langsamsten

#### Ausgabe-Verzeichnis
- Wählen Sie, wo separierte Stems gespeichert werden
- Standard: `temp/separated/`

#### Audio-Einstellungen
- **Sample-Rate**: 44100 Hz (Standard) oder 48000 Hz
- **Kanäle**: Stereo (2 Kanäle)

---

## Tipps und Best Practices

### Beste Ergebnisse erzielen

1. **Hochwertige Quelldateien verwenden**
   - WAV- oder FLAC-Dateien sind besser als MP3
   - Höhere Bitrate MP3s (320kbps) funktionieren besser als niedrigere Bitraten
   - Vermeiden Sie stark komprimierte oder niedrigqualitative Quellen

2. **Das richtige Modell wählen**
   - **Für Vocals**: Mel-RoFormer oder Ensemble-Modus
   - **Für Drums**: BS-RoFormer oder Demucs
   - **Für Piano/Gitarre**: Demucs v4 (6-stem)
   - **Für Geschwindigkeit**: Demucs v4 (4-stem)
   - **Für Qualität**: Quality Ensemble oder Ultra Ensemble

3. **Zeit managen**
   - Verarbeitung kann mehrere Minuten für lange Dateien dauern
   - Nutzen Sie den Warteschlange-Tab um mehrere Dateien über Nacht zu verarbeiten
   - Beginnen Sie mit kürzeren Dateien zum Testen der Qualität

4. **Dateien organisieren**
   - Benennen Sie Ausgabe-Ordner um, um Separationen zu verfolgen
   - Nutzen Sie beschreibende Namen für exportierte Mixe
   - Behalten Sie Originaldateien für erneute Verarbeitung mit anderen Modellen

5. **Experimentieren**
   - Probieren Sie verschiedene Modelle auf derselben Datei
   - Vergleichen Sie Ergebnisse um herauszufinden, was am besten für Ihren Anwendungsfall funktioniert
   - Ensemble-Modi liefern oft merklich bessere Qualität

### Hardware-Empfehlungen

**Für beste Performance:**
- **Apple Silicon Mac (M1/M2/M3)**: Schnellste Verarbeitung mit MPS-Beschleunigung
- **16 GB RAM oder mehr**: Handhabt große Dateien und Ensemble-Modi problemlos
- **SSD-Speicher**: Schnellere Datei-I/O während der Verarbeitung

**Minimum-Anforderungen:**
- **Intel Mac**: Funktioniert aber langsamer (besonders Ensemble-Modi)
- **8 GB RAM**: Ausreichend für die meisten Dateien, kann bei sehr langen Dateien Probleme haben
- **GPU deaktiviert**: Fällt auf CPU zurück (viel langsamer aber funktioniert)

### Häufige Workflows

#### Workflow 1: Karaoke-Tracks erstellen
1. Song im Upload-Tab laden
2. Beliebiges Modell wählen
3. "2-Stem (Karaoke)"-Modus wählen
4. Separieren
5. Instrumental-Stem für Karaoke nutzen

#### Workflow 2: Acapellas extrahieren
1. Song im Upload-Tab laden
2. "Mel-RoFormer" oder "Quality Ensemble" wählen
3. Separieren
4. Der Vocals-Stem ist Ihre Acapella

#### Workflow 3: Übungs-Tracks erstellen
1. Song separieren (4-stem oder 6-stem)
2. Stems im Player-Tab laden
3. Ihr Instrument stumm schalten (z.B. Gitarre muten)
4. Mix exportieren
5. Mit dem Custom-Backing-Track üben

#### Workflow 4: Sampling und Remixing
1. Song separieren (6-stem für mehr Optionen)
2. Stems im Player-Tab laden
3. Mit verschiedenen Kombinationen experimentieren
4. Interessante Abschnitte exportieren
5. In Ihrer DAW oder Ihrem Sampler verwenden

#### Workflow 5: Live-Sets aufnehmen
1. Aufnahme im Aufnahme-Tab starten
2. DJ-Set, Live-Performance oder Stream abspielen
3. Aufnahme stoppen und speichern
4. Aufnahme separieren
5. Spezifische Stems oder Abschnitte für spätere Verwendung extrahieren

---

## Fehlerbehebung

### Audio-Probleme

**Problem**: Kein Audio während der Wiedergabe im Player-Tab

**Lösungen**:
1. Prüfen Sie, dass die Audio-Ausgabe Ihres Macs nicht stumm geschaltet ist
2. Prüfen Sie Master-Lautstärke im Player-Tab
3. Prüfen Sie einzelne Stem-Lautstärken
4. Verifizieren Sie, dass Stems korrekt geladen wurden (alle Stem-Dateien sind gültige WAV-Dateien)
5. Starten Sie die App neu und laden Sie Stems erneut

---

**Problem**: Audio-Wiedergabe knistert oder ist verzerrt

**Lösungen**:
1. Master-Lautstärke reduzieren
2. Einzelne Stem-Lautstärken reduzieren (Clipping kann auftreten wenn alle Stems bei 100% sind)
3. Andere Audio-Anwendungen schließen
4. Activity Monitor auf hohe CPU-Auslastung prüfen
5. App neu starten

---

### Separations-Probleme

**Problem**: "GPU out of memory" Fehler

**Lösungen**:
1. Die App sollte automatisch auf CPU zurückfallen
2. Andere Anwendungen schließen um Speicher freizugeben
3. Falls Ensemble-Modus verwendet, versuchen Sie stattdessen ein einzelnes Modell
4. Chunk-Größe in erweiterten Einstellungen reduzieren
5. GPU in Einstellungen deaktivieren und CPU-Modus nutzen

---

**Problem**: Separation ist sehr langsam

**Lösungen**:
1. **GPU prüfen**: Stellen Sie sicher, dass GPU-Beschleunigung in Einstellungen aktiviert ist
2. **Schnelleres Modell wählen**: Demucs v4 (4-stem) ist am schnellsten
3. **Ensemble vermeiden**: Ensemble-Modi sind absichtlich langsamer für Qualität
4. **Andere Apps schließen**: CPU/GPU-Ressourcen freigeben
5. **Über Nacht verarbeiten**: Mehrere Dateien in Warteschlange und verarbeiten lassen

---

**Problem**: Schlechte Separations-Qualität (Vocals bluten durch, Artefakte)

**Lösungen**:
1. **Anderes Modell probieren**: Jedes Modell hat Stärken
2. **Ensemble-Modus nutzen**: Deutlich bessere Qualität
3. **Quellqualität prüfen**: Niedrigqualitative Eingabe = niedrigqualitative Ausgabe
4. **Ultra-Voreinstellung versuchen**: In Qualitätseinstellungen
5. **Manche Songs sind schwieriger**: Dichte Mixe und alte Aufnahmen sind herausfordernd

---

**Problem**: Modell-Download schlägt fehl

**Lösungen**:
1. Internet-Verbindung prüfen
2. App neu starten und erneut versuchen
3. Verfügbaren Festplattenspeicher prüfen (~1.5 GB für alle Modelle benötigt)
4. Versuchen Sie manuellen Download:
   ```bash
   python -c "from core.model_manager import get_model_manager; get_model_manager().download_model('mel-roformer')"
   ```

---

### Aufnahme-Probleme

**Problem**: "Kein Aufnahme-Backend verfügbar"

**Lösungen** (macOS 13+):
1. Bildschirmaufnahme-Berechtigung in Systemeinstellungen gewähren
2. Systemeinstellungen → Datenschutz & Sicherheit → Bildschirmaufnahme
3. Stem Separator aktivieren
4. App neu starten

**Lösungen** (macOS 12 und älter):
1. BlackHole installieren: `brew install blackhole-2ch`
2. "BlackHole 2ch" in Aufnahmegerät-Dropdown wählen
3. Audio-MIDI-Setup wie im Aufnahme-Abschnitt beschrieben konfigurieren

---

**Problem**: Aufnahme ist stumm (kein Audio erfasst)

**Lösungen** (macOS 13+):
1. Bildschirmaufnahme-Berechtigung ist gewährt verifizieren
2. Sicherstellen, dass Audio während Aufnahme tatsächlich abgespielt wird
3. System-Lautstärke ist nicht stumm geschaltet prüfen
4. App neu starten und erneut versuchen

**Lösungen** (macOS 12 und älter):
1. BlackHole ist installiert verifizieren
2. Multi-Output-Gerät-Setup in Audio-MIDI-Setup prüfen
3. Sicherstellen, dass System-Audio-Ausgabe auf Multi-Output-Gerät gesetzt ist
4. App neu starten

---

### Allgemeine Probleme

**Problem**: App stürzt ab oder friert ein

**Lösungen**:
1. Logs prüfen: `logs/app.log`
2. Nach Fehlermeldungen suchen
3. GPU in Einstellungen deaktivieren versuchen
4. Qualitäts-Voreinstellung auf "Standard" reduzieren
5. Zuerst kürzere Dateien verarbeiten
6. Falls anhaltend, GitHub-Issue mit Log-Auszügen erstellen

---

**Problem**: Dateien sind sehr groß (Stems belegen zu viel Platz)

**Erklärung**: Stems werden als unkomprimierte WAV-Dateien für Qualität gespeichert

**Lösungen**:
1. Nach dem Mischen zu MP3 exportieren um Platz zu sparen
2. Zwischen-Dateien (Logs, Cache) im temp/-Verzeichnis löschen
3. Nur finale gemischte Exports behalten
4. Externe Festplatte für Stem-Speicherung nutzen

---

### Hilfe bekommen

Falls Sie auf Probleme stoßen, die hier nicht abgedeckt sind:

1. **Logs prüfen**: `logs/app.log` enthält detaillierte Fehlermeldungen
2. **Debug-Modus aktivieren**: Setzen Sie `LOG_LEVEL = "DEBUG"` in `config.py`
3. **GitHub Issues**: [Issue erstellen](https://github.com/MaurizioFratello/StemSeparator/issues) mit:
   - Klarer Problembeschreibung
   - Schritten zur Reproduktion
   - Relevanten Log-Auszügen
   - System-Informationen (macOS-Version, Hardware)

---

## Tastatur-Shortcuts Referenz

| Shortcut | Aktion |
|----------|--------|
| ⌘ O | Datei öffnen |
| ⌘ , | Einstellungen öffnen |
| ⌘ Q | Anwendung beenden |
| Leertaste | Play/Pause |
| Escape | Wiedergabe stoppen |
| ⌘ E | Mixed Audio exportieren |
| M | Ausgewählten Stem muten |
| S | Ausgewählten Stem solo |

---

## Glossar

**Stem**: Eine isolierte Komponente eines Musik-Tracks (z.B. Vocals, Drums)

**Separation**: Der Prozess, eine gemischte Audio-Datei in einzelne Stems aufzuteilen

**Ensemble-Modus**: Mehrere KI-Modelle zusammen für überlegene Qualität nutzen

**Acapella**: Nur Vocal-Stem, ohne jegliches Instrumental

**Karaoke-Track**: Nur Instrumental, ohne Vocals

**GPU-Beschleunigung**: Grafikkarte für schnellere Verarbeitung nutzen (Apple Silicon MPS oder NVIDIA CUDA)

**Sample-Rate**: Audio-Auflösung in Samples pro Sekunde (44.1kHz = CD-Qualität)

**Bit-Tiefe**: Audio-Dynamikbereich-Auflösung (16-bit = Standard, 24-bit = professionell)

**Chunking**: Große Dateien in kleinere Segmente für Verarbeitung aufteilen

**Solo**: Nur einen Stem hören während alle anderen stumm geschaltet sind

**Mute**: Einen spezifischen Stem stumm schalten

---

<div align="center">

**Viel Erfolg beim Separieren!**

Für mehr Informationen besuchen Sie: [https://github.com/MaurizioFratello/StemSeparator](https://github.com/MaurizioFratello/StemSeparator)

</div>
