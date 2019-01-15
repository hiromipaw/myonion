# -*- coding: utf-8 -*-
"""
MyOnion | https://github.com/hiromipaw/myonion

Copyright (C) 2018 Hiro <hiro@torproject.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import queue
from PyQt5 import QtCore, QtWidgets, QtGui

from myonion import strings

class MyOnionGui(QtWidgets.QMainWindow):
    """
    MyOnionGui is the main window for the GUI that contains all of the
    GUI elements.
    """

    def __init__(self, common, qtapp, app):
        super(MyOnionGui, self).__init__()

        self.common = common
        self.common.log('MyOnionGui', '__init__')

        # self.onion = onion
        self.qtapp = qtapp
        self.app = app

        self.setWindowTitle('MyOnion')
        self.setWindowIcon(QtGui.QIcon(self.common.get_resource_path('images/logo.png')))
        self.setMinimumWidth(850)

        # System tray
        menu = QtWidgets.QMenu()
        self.settings_action = menu.addAction(strings._('gui_settings_window_title', True))
        exit_action = menu.addAction(strings._('systray_menu_exit', True))
        exit_action.triggered.connect(self.close)

        self.system_tray = QtWidgets.QSystemTrayIcon(self)
        # The convention is Mac systray icons are always grayscale
        if self.common.platform == 'Darwin':
            self.system_tray.setIcon(QtGui.QIcon(self.common.get_resource_path('images/logo_grayscale.png')))
        else:
            self.system_tray.setIcon(QtGui.QIcon(self.common.get_resource_path('images/logo.png')))
        self.system_tray.setContextMenu(menu)
        self.system_tray.show()

        # Buttons
        self.share_mode_button = QtWidgets.QPushButton(strings._('gui_mode_share_button', True));
        self.share_mode_button.setFixedHeight(50)
        self.share_mode_button.clicked.connect(self.share_mode_clicked)


        mode_switcher_layout = QtWidgets.QHBoxLayout();
        mode_switcher_layout.setSpacing(0)
        mode_switcher_layout.addWidget(self.share_mode_button)

        # Layouts)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(mode_switcher_layout)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.show()

    def share_mode_clicked(self):
        self.common.log('OnionShareGui', 'share_mode_clicked')
        self.update_mode_switcher()


    def update_mode_switcher(self):
        # Based on the current mode, switch the mode switcher button styles,
        # and show and hide widgets to switch modes
        self.share_mode_button.setStyleSheet(self.common.css['mode_switcher_selected_style'])
        self.app.start_onion_service()
