# -*- coding: utf-8 -*-
"""
MyOnion | https://github.com/hiromipaw/myonion

Copyright (C) 2018 hiro <hiro@torproject.org>

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

import os, sys, time, argparse, threading
from . import strings
from .common import Common
from .myonion import MyOnion

def main(cwd=None):
    """
    The main() function implements all of the logic that the command-line version of
    myonion uses.
    """

    common = Common()

    # print(strings._('version_string').format(common.version))

    # MyOnion CLI in OSX needs to change current working directory (#132)
    if common.platform == 'Darwin':
        if cwd:
            os.chdir(cwd)

    # Start the myonion app
    try:
        app = MyOnion(common)
        app.start_onion_service()
    except KeyboardInterrupt:
        print("")
        sys.exit()
