#!/usr/bin/env python3
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

import os, sys, platform, tempfile
from distutils.core import setup

def file_list(path):
    files = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            files.append(os.path.join(path, filename))
    return files

version = open('share/version.txt').read().strip()
description = (
    """MyOnion lets you securely and anonymously share a website from your computer. """
    """It works by starting a docker container, serving a website, making it """
    """ accessible as a Tor hidden service, and generating an unguessable URL to interact with it.""")
long_description = description + " " + (
    """It doesn't require setting up a server on the internet somewhere or using a third """
    """party hosting service. You host the website on your own computer and use a Tor """
    """hidden service to make it temporarily accessible over the internet. The other user """
    """just needs to use Tor Browser to visit your website."""
)
author = 'hiro'
author_email = 'hiro@torproject.org'
url = 'https://github.com/hiromipaw/myonion'
license = 'GPL v3'
keywords = 'onion, share, website, myonion, tor, anonymous, web server'
data_files=[
        (os.path.join(sys.prefix, 'share/applications'), ['install/myonion.desktop']),
        (os.path.join(sys.prefix, 'share/appdata'), ['install/myonion.appdata.xml']),
        (os.path.join(sys.prefix, 'share/pixmaps'), ['install/myonion80.xpm']),
        (os.path.join(sys.prefix, 'share/myonion'), file_list('share')),
        (os.path.join(sys.prefix, 'share/myonion/images'), file_list('share/images')),
        (os.path.join(sys.prefix, 'share/myonion/locale'), file_list('share/locale')),
        (os.path.join(sys.prefix, 'share/myonion/static/css'), file_list('share/static/css')),
        (os.path.join(sys.prefix, 'share/myonion/static/images'), file_list('share/static/images')),
        (os.path.join(sys.prefix, 'share/myonion/static/js'), file_list('share/static/js'))
    ]
if platform.system() != 'OpenBSD':
    data_files.append(('/usr/share/nautilus-python/extensions/', ['install/scripts/myonion-nautilus.py']))

setup(
    name='myonion', version=version,
    description=description, long_description=long_description,
    author=author, author_email=author_email,
    url=url, license=license, keywords=keywords,
    packages=['myonion', 'myonion_gui'],
    include_package_data=True,
    scripts=['install/scripts/myonion', 'install/scripts/myonion-gui'],
    data_files=data_files
)
