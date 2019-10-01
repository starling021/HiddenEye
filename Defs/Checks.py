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
    def verifyNetHunterConnection(self):
        """Needed to fix problem when HiddenEye under NetHunter don't have internet connection."""
        if(not environ.get('PYTHONHTTPSVERIFY', "") and getattr(ssl,  '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

    def exceptConnection(self, customHost, additionalText):
        def checkConnection(self, host='https://google.com'):  # Connection     check
            host = customHost
            text = additionalText
            system('clear')
            try:
                urlopen(host, timeout=10)
                print(_("{0}Internet is available.{1}").format(MAIN3, DEFAULT))
                return True
            except:
                return False
            checkConnection(host)

            if checkConnection(self, text) == False:
                print('''{1}
                _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
                |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
                |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}

                {0}[{1}!{0}]{1} ^Network error^. Verify your Internet connection.''' + '\n' + additionalText).format(MAIN0, MAIN4)
                exit(0)


def checkNgrok():  # Ngrok check
    if path.isfile('Server/ngrok') == False:  # Is Ngrok downloaded?
        print('[*] Ngrok Not Found !!')
        # Question where user must accept education purposes
        if input("\n{2}[{1}!{2}]{1} Do you accept installation of Ngrok? ({0}y{1}/{2}n{1})\n{2}HiddenEye >>> {0}").format(MAIN2, MAIN4, MAIN0).upper() != 'Y':
            system('clear')
            print('\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.PLEASE INSTALL NGROK!{1} ]\n\n').format(
                MAIN0, MAIN4)
            exit(0)
        else:
            print('[*] Downloading Ngrok...')
            if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
                filename = 'ngrok-stable-linux-arm.zip'
            else:
                ostype = systemos().lower()
                if architecture()[0] == '64bit':
                    filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
                else:
                    filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
            url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
            download(url)
            system('unzip ' + filename)
            system('mv ngrok Server/ngrok')
            system('rm -Rf ' + filename)
            system('clear')


class PermissionsManager:
    def checkPermissions(self):
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
