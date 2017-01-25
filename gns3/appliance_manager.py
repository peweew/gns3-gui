#!/usr/bin/env python
#
# Copyright (C) 2016 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json


class ApplianceManager:

    def __init__(self):
        self._appliances = []

        # TEMPORARY: For tests
        # import os
        # path = "/Users/noplay/code/gns3/gns3-registry/appliances"
        # for appliance in os.listdir(path):
        #     with open(os.path.join(path, appliance)) as f:
        #         self._appliances.append(json.load(f))
        # return
        self._appliances.append(json.loads("""{
    "name": "Micro Core Linux",
    "category": "guest",
    "description": "Micro Core Linux is a smaller variant of Tiny Core without a graphical desktop.This is complete Linux system needing few resources to run.",
    "vendor_name": "Team Tiny Core",
    "vendor_url": "http://distro.ibiblio.org/tinycorelinux",
    "documentation_url": "http://wiki.tinycorelinux.net/",
    "product_name": "Micro Core Linux",
    "product_url": "http://distro.ibiblio.org/tinycorelinux",
    "registry_version": 3,
    "status": "stable",
    "maintainer": "GNS3 Team",
    "maintainer_email": "developers@gns3.net",
    "usage": "For version >= 6.4, login/password is gns3. For older version it is tc. Note that sudo works without any password",
    "symbol": "linux_guest.svg",
    "qemu": {
        "adapter_type": "e1000",
        "adapters": 1,
        "ram": 64,
        "arch": "i386",
        "console_type": "telnet",
        "kvm": "allow"
    },
    "images": [
        {
            "filename": "linux-microcore-6.4.img",
            "version": "6.4",
            "md5sum": "877419f975c4891c019947ceead5c696",
            "filesize": 16580608,
            "download_url": "https://sourceforge.net/projects/gns-3/files/Qemu%20Appliances/",
            "direct_download_url": "http://downloads.sourceforge.net/project/gns-3/Qemu%20Appliances/linux-microcore-6.4.img"
        },
        {
            "filename": "linux-microcore-4.0.2-clean.img",
            "version": "4.0.2",
            "md5sum": "e13d0d1c0b3999ae2386bba70417930c",
            "filesize": 26411008,
            "download_url": "https://sourceforge.net/projects/gns-3/files/Qemu%20Appliances/",
            "direct_download_url": "http://downloads.sourceforge.net/project/gns-3/Qemu%20Appliances/linux-microcore-4.0.2-clean.img"
        },
        {
            "filename": "linux-microcore-3.4.1.img",
            "version": "3.4.1",
            "md5sum": "fa2ec4b1fffad67d8103c3391bbf9df2",
            "filesize": 24969216,
            "download_url": "https://sourceforge.net/projects/gns-3/files/Qemu%20Appliances/",
            "direct_download_url": "http://downloads.sourceforge.net/project/gns-3/Qemu%20Appliances/linux-microcore-3.4.1.img"
        }
    ],
    "versions": [
        {
            "name": "6.4",
            "images": {
                "hda_disk_image": "linux-microcore-6.4.img"
            }
        },
        {
            "name": "4.0.2",
            "images": {
                "hda_disk_image": "linux-microcore-4.0.2-clean.img"
            }
        },
        {
            "name": "3.4.1",
            "images": {
                "hda_disk_image": "linux-microcore-3.4.1.img"
            }
        }
    ]
}"""))
        self._appliances.append(json.loads("""
{
    "name": "Alpine Linux",
    "category": "guest",
    "description": "Alpine Linux is a security-oriented, lightweight Linux distribution based on musl libc and busybox.",
    "vendor_name": "Alpine Linux Development Team",
    "vendor_url": "http://alpinelinux.org",
    "documentation_url": "http://wiki.alpinelinux.org",
    "product_name": "Alpine Linux",
    "registry_version": 1,
    "status": "experimental",
    "availability": "free",
    "maintainer": "GNS3 Team",
    "maintainer_email": "developers@gns3.net",
    "usage": "User is root. Password is gns3",
    "symbol": "linux_guest.svg",
    "qemu": {
        "adapter_type": "e1000",
        "adapters": 1,
        "ram": 32,
        "arch": "x86_64",
        "console_type": "telnet",
        "kvm": "allow"
    },
    "images": [
        {
            "filename": "alpine-linux-3.2.3.qcow2",
            "version": "3.2.3",
            "md5sum": "b82d895ecba270ecc5e5b445ec53ee02",
            "filesize": 143065088,
            "download_url": "https://sourceforge.net/projects/gns-3/files/Qemu%20Appliances/",
            "direct_download_url": "http://downloads.sourceforge.net/project/gns-3/Qemu%20Appliances/alpine-linux-3.2.3.qcow2"
        }
    ],
    "versions": [
        {
            "name": "3.2.3",
            "images": {
                "hda_disk_image": "alpine-linux-3.2.3.qcow2"
            }
        }
    ]
}
    """))

    def appliances(self):
        return self._appliances

    @staticmethod
    def instance():
        """
        Singleton to return only on instance of ApplianceManager.
        :returns: instance of ApplianceManager
        """

        if not hasattr(ApplianceManager, '_instance') or ApplianceManager._instance is None:
            ApplianceManager._instance = ApplianceManager()
        return ApplianceManager._instance
