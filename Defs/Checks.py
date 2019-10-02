# Checks functions

from urllib.request import urlopen
from os import getuid, environ, system, path
from subprocess import check_output
from platform import system as systemos, architecture
from wget import download
import os
import ctypes
import ssl
from Defs.ThemesManager import ThemeManager

colorTheme = ThemeManager().colorSelector()
MAIN0, MAIN1, MAIN2, MAIN3, MAIN4 = colorTheme[0], colorTheme[
    1], colorTheme[2], colorTheme[3],  colorTheme[4]


class ConnectionManager:
    def verifyNetHunterConnection():
        """Needed to fix problem when HiddenEye under NetHunter don't have internet connection."""
        if(not environ.get('PYTHONHTTPSVERIFY', "") and getattr(ssl,  '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

    def confirmConnection(host='https://google.com'):
        system('clear')
        try:
            urlopen(host, timeout=10)
            print("{0}Internet is available.{1}".format(MAIN3, MAIN4))
            return True
        except:
            print('''{1}
            _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
            |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
            |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}

            {0}[{1}!{0}]{1} ^Network error^. Verify your Internet connection.\n'''.format(MAIN0, MAIN4))
            exit(0)


class PermissionsManager:
    def checkPermissions():
        if systemos() == 'Linux':
            if getuid() == 0:
                print("{0}Permissions granted!".format(MAIN3))
            else:
                raise PermissionError(
                    "{0}Permissions denied! Please run as '{1}sudo{0}'".format(MAIN0, MAIN3))
        elif systemos() == 'Windows':
            if ctypes.windll.shell32.IsUserAnAdmin() != 0:
                print("{0}Permissions granted!".format(MAIN3))
            else:
                raise PermissionError(
                    "{0}Permissions denied! Please run as     Administrator".format(MAIN0))
        elif systemos() == 'Darwin':
            if getuid() == 0:
                print("{0}Permissions granted!".format(MAIN3))
            else:
                raise PermissionError(
                    "{0}Permissions denied! Please run as '{1}sudo{0}'".format(MAIN0, MAIN3))
        else:
            raise PermissionError(
                "{0}Permissions denied! Unsupported platform".format(MAIN0))
