# Primitive config
import configparser
import os


class ConfigurationManager:
    def createConfig(path="Settings.ini"):
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.add_section("Defaults")
        # config.set("Settings", "Language", "en") #TODO LANGUAGE SYSTEM WILL BE IMPLEMENTED LATER
        config.set("Settings", "DidBackground", "True")
        config.set("Defaults", "webPage", "Facebook")
        config.set("Defaults", "additionalOption", "1")
        config.set("Defaults", "theme", "anaglyph")
        with open(path, 'w') as configFile:
            config.write(configFile)

    def readConfig(path="Settings.ini"):
        config = configparser.ConfigParser()
        config.read(path)
        return config

    def confirmSettingsExistence():
        if not os.path.exists("Settings.ini"):
            ConfigurationManager.createConfig()
