# Themes Manager TODO
# NEW THEMES SYSTEM WILL BE IMPLEMENTED SOON
# PLEASE DON'T WORRY ABOUT FIXING THIS GARBAGE
import sys
from Defs.Configurations import ConfigurationManager

color = [0, 0, 0, 0, 0]
config = ConfigurationManager.readConfig()


class ThemesManager:
    def selectTheme():
        ConfigurationManager.confirmSettingsExistence()
        for arg in sys.argv:
            if arg in ['--theme']:
                for arg in sys.argv:
                    if arg in ['anaglyph', '3danaglyph', '3Danaglyph', '3DAnaglyph']:
                        # LightRed, BackgroundCyan, Cyan, Green, ResetAll
                        color = ['\033[91m', '\033[46m',
                                 '\033[36m', '\033[32m',  '\033[0m']
                        if arg in ['--default']:
                            config.set("Defaults", "theme", "anaglyph")
                        return color
                    if arg in ['ocean', 'breeze', 'blue']:
                        # Cyan, BackgroundCyan, BrightBlue, DarkGray, ResetAll
                        color = ['\033[36m', '\033[46m',
                                 '\033[34m', '\033[30m', '\033[0m']
                        if arg in ['--default']:
                            config.set("Defaults", "theme", "ocean")
                        return color
        if config.get("Defaults", "theme") == "anaglyph":
            # LightRed, BackgroundCyan, Cyan, Green, ResetAll
            color = ['\033[91m', '\033[46m',
                     '\033[36m', '\033[32m',  '\033[0m']
            return color
        elif config.get("Defaults", "theme") == "ocean":
            # Cyan, BackgroundCyan, BrightBlue, DarkGray, ResetAll
            color = ['\033[36m', '\033[46m', '\033[34m', '\033[30m', '\033[0m']
            return color
