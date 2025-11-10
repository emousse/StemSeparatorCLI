"""
Player Widget - Stem playback and mixing

PURPOSE: Allow users to play back separated stems with individual volume/mute/solo controls.
CONTEXT: Provides mixing interface for separated audio stems.
"""
from pathlib import Path
from typing import Optional, Dict
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QSlider, QGroupBox, QFileDialog, QMessageBox, QListWidget,
    QListWidgetItem
)
from PySide6.QtCore import Qt, Signal, Slot

from ui.app_context import AppContext


class StemControl(QWidget):
    """
    Individual stem control with volume, mute, solo
    
    WHY: Encapsulates per-stem mixing controls for cleaner layout
    """
    
    mute_changed = Signal(bool)  # is_muted
    solo_changed = Signal(bool)  # is_solo
    volume_changed = Signal(int)  # volume (0-100)
    
    def __init__(self, stem_name: str, parent=None):
        super().__init__(parent)
        self.stem_name = stem_name
        self.is_muted = False
        self.is_solo = False
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup stem control layout"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Stem name
        name_label = QLabel(self.stem_name.capitalize())
        name_label.setMinimumWidth(80)
        layout.addWidget(name_label)
        
        # Mute button
        self.btn_mute = QPushButton("M")
        self.btn_mute.setCheckable(True)
        self.btn_mute.setMaximumWidth(30)
        self.btn_mute.clicked.connect(self._on_mute_clicked)
        layout.addWidget(self.btn_mute)
        
        # Solo button
        self.btn_solo = QPushButton("S")
        self.btn_solo.setCheckable(True)
        self.btn_solo.setMaximumWidth(30)
        self.btn_solo.clicked.connect(self._on_solo_clicked)
        layout.addWidget(self.btn_solo)
        
        # Volume slider
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(75)
        self.volume_slider.valueChanged.connect(self.volume_changed.emit)
        layout.addWidget(self.volume_slider)
        
        # Volume label
        self.volume_label = QLabel("75%")
        self.volume_label.setMinimumWidth(40)
        self.volume_slider.valueChanged.connect(
            lambda v: self.volume_label.setText(f"{v}%")
        )
        layout.addWidget(self.volume_label)
    
    @Slot()
    def _on_mute_clicked(self):
        """Handle mute button click"""
        self.is_muted = self.btn_mute.isChecked()
        self.mute_changed.emit(self.is_muted)
        
        # Update style
        if self.is_muted:
            self.btn_mute.setStyleSheet("background-color: red;")
        else:
            self.btn_mute.setStyleSheet("")
    
    @Slot()
    def _on_solo_clicked(self):
        """Handle solo button click"""
        self.is_solo = self.btn_solo.isChecked()
        self.solo_changed.emit(self.is_solo)
        
        # Update style
        if self.is_solo:
            self.btn_solo.setStyleSheet("background-color: green;")
        else:
            self.btn_solo.setStyleSheet("")


class PlayerWidget(QWidget):
    """
    Widget for playing and mixing separated stems
    
    Features:
    - Load separated stems
    - Individual volume control per stem
    - Mute/solo per stem
    - Master volume
    - Playback controls (play/pause/stop)
    - Position slider
    - Export mixed audio
    
    NOTE: Full implementation would require audio playback library (sounddevice, PyAudio, or Qt Multimedia)
    For now, this provides the UI structure with stubs for actual playback.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ctx = AppContext()
        self.stem_files: Dict[str, Path] = {}
        self.stem_controls: Dict[str, StemControl] = {}
        self.is_playing = False
        
        self._setup_ui()
        self._connect_signals()
        self.apply_translations()
        
        self.ctx.logger().info("PlayerWidget initialized")
    
    def _setup_ui(self):
        """Setup widget layout"""
        layout = QVBoxLayout(self)
        
        # File Loading Group
        load_group = QGroupBox("Load Stems")
        load_layout = QVBoxLayout()
        
        # Recent files list
        self.stems_list = QListWidget()
        self.stems_list.setMaximumHeight(100)
        load_layout.addWidget(self.stems_list)
        
        # Load buttons
        load_buttons = QHBoxLayout()
        self.btn_load_dir = QPushButton("Load from Directory")
        self.btn_load_files = QPushButton("Load Individual Files")
        load_buttons.addWidget(self.btn_load_dir)
        load_buttons.addWidget(self.btn_load_files)
        load_buttons.addStretch()
        load_layout.addLayout(load_buttons)
        
        load_group.setLayout(load_layout)
        layout.addWidget(load_group)
        
        # Mixer Group
        mixer_group = QGroupBox("Mixer")
        mixer_layout = QVBoxLayout()
        
        self.stems_container = QVBoxLayout()
        mixer_layout.addLayout(self.stems_container)
        
        # Master volume
        master_layout = QHBoxLayout()
        master_layout.addWidget(QLabel("Master Volume:"))
        self.master_slider = QSlider(Qt.Horizontal)
        self.master_slider.setRange(0, 100)
        self.master_slider.setValue(100)
        master_layout.addWidget(self.master_slider)
        self.master_label = QLabel("100%")
        self.master_slider.valueChanged.connect(
            lambda v: self.master_label.setText(f"{v}%")
        )
        master_layout.addWidget(self.master_label)
        mixer_layout.addLayout(master_layout)
        
        mixer_group.setLayout(mixer_layout)
        layout.addWidget(mixer_group)
        
        # Playback Controls Group
        controls_group = QGroupBox("Playback")
        controls_layout = QVBoxLayout()
        
        # Position slider (disabled until playback implemented)
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setEnabled(False)
        controls_layout.addWidget(self.position_slider)
        
        # Time labels
        time_layout = QHBoxLayout()
        self.current_time_label = QLabel("00:00")
        self.duration_label = QLabel("00:00")
        time_layout.addWidget(self.current_time_label)
        time_layout.addStretch()
        time_layout.addWidget(self.duration_label)
        controls_layout.addLayout(time_layout)
        
        # Control buttons
        buttons_layout = QHBoxLayout()
        self.btn_play = QPushButton("Play")
        self.btn_play.setEnabled(False)
        self.btn_pause = QPushButton("Pause")
        self.btn_pause.setEnabled(False)
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.setEnabled(False)
        self.btn_export = QPushButton("Export Mixed Audio")
        self.btn_export.setEnabled(False)
        
        buttons_layout.addWidget(self.btn_play)
        buttons_layout.addWidget(self.btn_pause)
        buttons_layout.addWidget(self.btn_stop)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.btn_export)
        controls_layout.addLayout(buttons_layout)
        
        controls_group.setLayout(controls_layout)
        layout.addWidget(controls_group)
        
        # Info label
        self.info_label = QLabel(
            "Load separated stems to use the mixer.\n\n"
            "NOTE: Full playback functionality requires audio backend integration."
        )
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)
        
        layout.addStretch()
    
    def _connect_signals(self):
        """Connect signals"""
        self.btn_load_dir.clicked.connect(self._on_load_dir)
        self.btn_load_files.clicked.connect(self._on_load_files)
        self.btn_play.clicked.connect(self._on_play)
        self.btn_pause.clicked.connect(self._on_pause)
        self.btn_stop.clicked.connect(self._on_stop)
        self.btn_export.clicked.connect(self._on_export)
    
    @Slot()
    def _on_load_dir(self):
        """
        Load all stems from directory
        
        WHY: Typical workflow is to load all stems from a separation output directory
        """
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Directory with Stems"
        )
        
        if not directory:
            return
        
        dir_path = Path(directory)
        
        # Find audio files
        file_manager = self.ctx.file_manager()
        audio_files = file_manager.list_audio_files(dir_path)
        
        if not audio_files:
            QMessageBox.warning(
                self,
                "No Audio Files",
                f"No supported audio files found in:\n{dir_path}"
            )
            return
        
        self._load_stems(audio_files)
    
    @Slot()
    def _on_load_files(self):
        """Load individual stem files"""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Audio Files (*.wav *.mp3 *.flac *.m4a *.ogg *.aac)")
        
        if file_dialog.exec():
            file_paths = [Path(f) for f in file_dialog.selectedFiles()]
            self._load_stems(file_paths)
    
    def _load_stems(self, file_paths: list[Path]):
        """
        Load stem files into player
        
        WHY: Parses stem names from filenames and creates mixer controls
        """
        self.stem_files.clear()
        
        # Clear existing controls
        for control in self.stem_controls.values():
            control.deleteLater()
        self.stem_controls.clear()
        
        # Clear stems list
        self.stems_list.clear()
        
        # Load each file
        for file_path in file_paths:
            # Try to extract stem name from filename
            # Expected format: "songname_vocals.wav" or "vocals.wav"
            name_parts = file_path.stem.split('_')
            if len(name_parts) > 1:
                stem_name = name_parts[-1]
            else:
                stem_name = file_path.stem
            
            self.stem_files[stem_name] = file_path
            
            # Add to list
            self.stems_list.addItem(f"{stem_name}: {file_path.name}")
            
            # Create control
            control = StemControl(stem_name, self)
            self.stem_controls[stem_name] = control
            self.stems_container.addWidget(control)
            
            self.ctx.logger().info(f"Loaded stem: {stem_name} from {file_path.name}")
        
        # Enable playback controls
        has_stems = len(self.stem_files) > 0
        self.btn_play.setEnabled(has_stems)
        self.btn_export.setEnabled(has_stems)
        
        if has_stems:
            self.info_label.setText(
                f"Loaded {len(self.stem_files)} stems.\n\n"
                "Playback requires audio backend integration (not yet implemented)."
            )
        
        self.ctx.logger().info(f"Loaded {len(self.stem_files)} stems total")
    
    @Slot()
    def _on_play(self):
        """
        Start playback
        
        WHY: Would trigger actual audio playback with volume/mute/solo applied
        NOTE: Stub - requires audio playback backend
        """
        QMessageBox.information(
            self,
            "Playback Not Implemented",
            "Audio playback requires integration with an audio backend "
            "(sounddevice, PyAudio, or Qt Multimedia).\n\n"
            "This is planned for a future update."
        )
        
        self.ctx.logger().info("Playback requested (not implemented)")
    
    @Slot()
    def _on_pause(self):
        """Pause playback"""
        # Stub for future implementation
        pass
    
    @Slot()
    def _on_stop(self):
        """Stop playback"""
        # Stub for future implementation
        pass
    
    @Slot()
    def _on_export(self):
        """
        Export mixed audio to file
        
        WHY: Allows saving the custom mix with applied volume/mute settings
        NOTE: Stub - requires audio mixing backend
        """
        if not self.stem_files:
            return
        
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Mixed Audio",
            "",
            "WAV Files (*.wav);;FLAC Files (*.flac)"
        )
        
        if not save_path:
            return
        
        QMessageBox.information(
            self,
            "Export Not Implemented",
            "Audio mixing and export requires implementation of:\n"
            "1. Load all stems into memory\n"
            "2. Apply volume/mute/solo settings\n"
            "3. Mix down to stereo\n"
            "4. Save to file\n\n"
            "This is planned for a future update."
        )
        
        self.ctx.logger().info(f"Export requested to {save_path} (not implemented)")
    
    def load_separation_result(self, stems: Dict[str, Path]):
        """
        Load stems from separation result
        
        WHY: Allows direct loading from separation output
        """
        if stems:
            self._load_stems(list(stems.values()))
    
    def apply_translations(self):
        """Apply current language translations"""
        # Translation keys would be defined in resources/translations/*.json
        pass

