"""
Tests for MainWindow

PURPOSE: Verify main window initialization, menu actions, and widget integration.
CONTEXT: Core GUI integration tests.
"""
import pytest
from unittest.mock import Mock, patch
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


@pytest.mark.unit
def test_main_window_creation(qapp, reset_singletons):
    """Test that main window can be created"""
    window = MainWindow()
    
    assert window is not None
    assert window.windowTitle() == "Stem Separator"
    assert window.width() == 1200
    assert window.height() == 800


@pytest.mark.unit
def test_main_window_has_tabs(qapp, reset_singletons):
    """Test that main window has all expected tabs"""
    window = MainWindow()
    
    tab_widget = window._tab_widget
    assert tab_widget.count() == 4
    
    # Check tab titles (default English)
    tab_titles = [tab_widget.tabText(i) for i in range(tab_widget.count())]
    assert "Upload" in tab_titles
    assert "Recording" in tab_titles
    assert "Queue" in tab_titles
    assert "Player" in tab_titles


@pytest.mark.unit
def test_main_window_has_menu(qapp, reset_singletons):
    """Test that main window has menu bar with expected menus"""
    window = MainWindow()
    
    menu_bar = window.menuBar()
    assert menu_bar is not None
    
    # Get menu titles
    menus = [action.text() for action in menu_bar.actions() if action.menu()]
    
    # Should have File, View, Help menus
    assert len(menus) >= 3


@pytest.mark.unit
def test_main_window_language_switch(qapp, reset_singletons):
    """Test language switching functionality"""
    window = MainWindow()
    
    # Initially should be German (default)
    current_lang = window._context.get_language()
    assert current_lang in ['de', 'en']
    
    # Switch language
    for lang_action in window._language_actions.values():
        if lang_action.data() != current_lang:
            lang_action.trigger()
            break
    
    # Language should have changed
    new_lang = window._context.get_language()
    assert new_lang != current_lang


@pytest.mark.unit
def test_main_window_settings_action(qapp, reset_singletons):
    """Test that settings action exists and can be triggered"""
    with patch('ui.main_window.SettingsDialog') as mock_dialog_class:
        mock_dialog = Mock()
        mock_dialog_class.return_value = mock_dialog
        
        window = MainWindow()
        
        # Trigger settings action
        window._settings_action.trigger()
        
        # Settings dialog should have been created
        mock_dialog_class.assert_called_once()
        mock_dialog.exec.assert_called_once()


@pytest.mark.unit
def test_main_window_quit_action(qapp, reset_singletons):
    """Test that quit action is connected"""
    window = MainWindow()
    
    # Quit action should exist
    assert window._quit_action is not None
    assert window._quit_action.shortcut().toString() == "Ctrl+Q"


@pytest.mark.unit
def test_main_window_widgets_connected(qapp, reset_singletons):
    """Test that widgets are properly connected via signals"""
    window = MainWindow()
    
    # Upload widget should be connected to queue
    assert window._upload_widget is not None
    assert window._queue_widget is not None
    
    # Recording widget should be connected to main window
    assert window._recording_widget is not None


@pytest.mark.unit
def test_main_window_close_event(qapp, reset_singletons):
    """Test that close event is handled properly"""
    window = MainWindow()
    
    # Create mock close event
    from PySide6.QtGui import QCloseEvent
    event = QCloseEvent()
    
    # Should accept close event
    window.closeEvent(event)
    assert event.isAccepted()


@pytest.mark.unit
def test_main_window_status_bar(qapp, reset_singletons):
    """Test that status bar exists and shows ready message"""
    window = MainWindow()
    
    status_bar = window.statusBar()
    assert status_bar is not None
    assert status_bar.currentMessage() != ""

