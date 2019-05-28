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
from __future__ import division
import os
import sys
import platform
import argparse
import signal
from PyQt5 import QtCore, QtWidgets

from myonion import strings
from myonion.common import Common
from myonion.myonion import MyOnion

from .myonion_gui import MyOnionGui

class Application(QtWidgets.QApplication):
    """
    This is Qt's QApplication class. It has been overridden to support threads
    and the quick keyboard shortcut.
    """
    def __init__(self, common):
        if common.platform == 'Linux' or common.platform == 'BSD':
            self.setAttribute(QtCore.Qt.AA_X11InitThreads, True)
        QtWidgets.QApplication.__init__(self, sys.argv)
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            event.key() == QtCore.Qt.Key_Q and
            event.modifiers() == QtCore.Qt.ControlModifier):
                self.quit()
        return False


def main():
    """
    The main() function implements all of the logic that the GUI version of onionshare uses.
    """
    common = Common()
    common.define_css()

    strings.load_strings(common)
    print(strings._('version_string').format(common.version))

    # Allow Ctrl-C to smoothly quit the program instead of throwing an exception
    # https://stackoverflow.com/questions/42814093/how-to-handle-ctrlc-in-python-app-with-pyqt
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Start the Qt app
    global qtapp
    qtapp = Application(common)

    # config = args.config

    # local_only = bool(args.local_only)
    # debug = bool(args.debug)

    # Debug mode?
    # common.debug = debug

    # Start the MyOnion app
    app = MyOnion(common)

    # Launch the gui
    gui = MyOnionGui(common, qtapp, app)

    # Clean up when app quits
    def shutdown():
        # Define cleanup function
        app.cleanup()
    qtapp.aboutToQuit.connect(shutdown)

    # All done
    sys.exit(qtapp.exec_())

if __name__ == '__main__':
    main()
