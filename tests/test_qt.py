import pytest
from PyQt5 import QtCore
from PyQt5.Qt import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QFileDialog, QDialogButtonBox

from qt.settings import SettingsWindow



class TestSettingsWindow:
    def test_settings_window_initial_state(self, qtbot):
        settings_window = SettingsWindow()
        settings_window.show()
        qtbot.addWidget(settings_window)
        assert settings_window.download_location_hint.text() == 'Location to be shown here'

