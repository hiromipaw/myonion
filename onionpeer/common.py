
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
import base64
import hashlib
import inspect
import os
import platform
import random
import socket
import sys
import tempfile
import threading
import time

class Common(object):
    """
    The Common object is shared amongst all parts of MyOnion.
    """
    def __init__(self, debug=False):
        self.debug = debug

        # The platform MyOnion is running on
        self.platform = platform.system()
        if self.platform.endswith('BSD'):
            self.platform = 'BSD'

        # The current version of MyOnion
        with open(self.get_resource_path('version.txt')) as f:
            self.version = f.read().strip()

    def log(self, module, func, msg=None):
        """
        If debug mode is on, log error messages to stdout
        """
        final_msg = ""
        if self.debug:
            timestamp = time.strftime("%b %d %Y %X")

            final_msg = "[{}] {}.{}".format(timestamp, module, func)
            if msg:
                final_msg = '{}: {}'.format(final_msg, msg)
        print(final_msg)

    def get_resource_path(self, filename):
        """
        Returns the absolute path of a resource, regardless of whether MyOnion is installed
        systemwide, and whether regardless of platform
        """
        # On Windows, and in Windows dev mode, switch slashes in incoming filename to backslackes
        if self.platform == 'Windows':
            filename = filename.replace('/', '\\')

        if getattr(sys, 'myonion_dev_mode', False):
            # Look for resources directory relative to python file
            prefix = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 'share')
            if not os.path.exists(prefix):
                # While running tests during stdeb bdist_deb, look 3 directories up for the share folder
                prefix = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(prefix)))), 'share')

        elif self.platform == 'BSD' or self.platform == 'Linux':
            # Assume MyOnion is installed systemwide in Linux, since we're not running in dev mode
            prefix = os.path.join(sys.prefix, 'share/myonion')

        elif getattr(sys, 'frozen', False):
            # Check if app is "frozen"
            # https://pythonhosted.org/PyInstaller/#run-time-information
            if self.platform == 'Darwin':
                prefix = os.path.join(sys._MEIPASS, 'share')
            elif self.platform == 'Windows':
                prefix = os.path.join(os.path.dirname(sys.executable), 'share')

        return os.path.join(prefix, filename)

    def define_css(self):
        """
        This defines all of the stylesheets used in GUI mode, to avoid repeating code.
        This method is only called in GUI mode.
        """
        self.css = {
            # OnionShareGui styles
            'mode_switcher_selected_style': """
                QPushButton {
                    color: #ffffff;
                    background-color: #4e064f;
                    border: 0;
                    border-right: 1px solid #69266b;
                    font-weight: bold;
                    border-radius: 0;
                }""",

            'mode_switcher_unselected_style': """
                QPushButton {
                    color: #ffffff;
                    background-color: #601f61;
                    border: 0;
                    font-weight: normal;
                    border-radius: 0;
                }""",

            'settings_button': """
                QPushButton {
                    background-color: #601f61;
                    border: 0;version
                    border-left: 1px solid #69266b;
                    border-radius: 0;
                }""",

            'server_status_indicator_label': """
                QLabel {
                    font-style: italic;
                    color: #666666;
                    padding: 2px;
                }""",

            'status_bar': """
                QStatusBar {
                    font-style: italic;
                    color: #666666;
                }
                QStatusBar::item {
                    border: 0px;
                }""",

            # Common styles between ShareMode and ReceiveMode and their child widgets
            'mode_info_label': """
                QLabel {
                    font-size: 12px;
                    color: #666666;
                }
                """,

            'server_status_url': """
                QLabel {
                    background-color: #ffffff;
                    color: #000000;
                    padding: 10px;
                    border: 1px solid #666666;
                }
                """,

            'server_status_url_buttons': """
                QPushButton {
                    color: #3f7fcf;
                }
                """,

            'server_status_button_stopped': """
                QPushButton {
                    background-color: #5fa416;
                    color: #ffffff;
                    padding: 10px;
                    border: 0;
                    border-radius: 5px;
                }""",

            'server_status_button_working': """
                QPushButton {
                    background-color: #4c8211;
                    color: #ffffff;
                    padding: 10px;
                    border: 0;
                    border-radius: 5px;
                    font-style: italic;
                }""",

            'server_status_button_started': """
                QPushButton {
                    background-color: #d0011b;
                    color: #ffffff;
                    padding: 10px;
                    border: 0;
                    border-radius: 5px;
                }""",

            'downloads_uploads_label': """
                QLabel {
                    font-weight: bold;
                    font-size 14px;
                    text-align: center;
                }""",

            'downloads_uploads_progress_bar': """
                QProgressBar {
                    border: 1px solid #4e064f;
                    background-color: #ffffff !important;
                    text-align: center;
                    color: #9b9b9b;
                    font-size: 12px;
                }
                QProgressBar::chunk {
                    background-color: #4e064f;
                    width: 10px;
                }""",

            # Share mode and child widget styles
            'share_zip_progess_bar': """
                QProgressBar {
                    border: 1px solid #4e064f;
                    background-color: #ffffff !important;
                    text-align: center;
                    color: #9b9b9b;
                }
                QProgressBar::chunk {
                    border: 0px;
                    background-color: #4e064f;
                    width: 10px;
                }""",

            'share_filesize_warning': """
                QLabel {
                    padding: 10px 0;
                    font-weight: bold;
                    color: #333333;
                }
                """,

            'share_file_selection_drop_here_label': """
                QLabel {
                    color: #999999;
                }""",

            'share_file_selection_drop_count_label': """
                QLabel {
                    color: #ffffff;
                    background-color: #f44449;
                    font-weight: bold;
                    padding: 5px 10px;
                    border-radius: 10px;
                }""",

            'share_file_list_drag_enter': """
                FileList {
                    border: 3px solid #538ad0;
                }
                """,

            'share_file_list_drag_leave': """
                FileList {
                    border: none;
                }
                """,

            'share_file_list_item_size': """
                QLabel {
                    color: #666666;
                    font-size: 11px;
                }""",

            # Receive mode and child widget styles
            'receive_file': """
                QWidget {
                    background-color: #ffffff;
                }
                """,

            'receive_file_size': """
                QLabel {
                    color: #666666;
                    font-size: 11px;
                }""",

            # Settings dialog
            'settings_version': """
                QLabel {
                    color: #666666;
                }""",

            'settings_tor_status': """
                QLabel {
                    background-color: #ffffff;
                    color: #000000;
                    padding: 10px;
                }""",

            'settings_whats_this': """
                QLabel {
                    font-size: 12px;
                }"""
        }
