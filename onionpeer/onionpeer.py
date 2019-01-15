
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

import os, shutil, docker

from . import common

class MyOnion(object):
    """
    MyOnion is the main application class. Pass in options and run
    start_onion_service and it will do the magic.
    """

    def __init__(self, common):
        """
        Init settings
        """
        self.common = common

        self.common.log('MyOnion', '__init__')

    def start_onion_service(self):
        """
        Start the myonion onion service.
        """

        api_client = docker.APIClient(base_url='unix://var/run/docker.sock')

        client = docker.from_env()
        print("Building docker container ... \n")

        build = [line for line in api_client.build(path=self.common.get_resource_path('containers/website'), tag='website', dockerfile='./Dockerfile')]

        container = client.containers.run('website:latest', detach=True, tty=True)

        print("\nRunning nginx ... \n ")
        nginx = container.exec_run('nginx', user='root', stdout=True, stderr=True, detach=True).output
        print(container.logs())

        print("\nRunning tor ... \n ")
        nginx = container.exec_run('tor', user='root', stdout=True, stderr=True, detach=True).output
        print(container.logs())

        onion = container.exec_run('cat onion_web_service/hostname', user='root').output

        container.exec_run('sed -i -e \'s/server_name _/server_name 746ts4dkulh6zoo5.onion/g\' /etc/nginx/sites-available/default', user='root')

        print("\nPlease connect via Tor Browser to the following .onion address \n")
        print(onion)
