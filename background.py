import json
import urllib.request
import time
import os
import shutil
from colorama import Fore, Back, Style
from datetime import date, datetime
from ast import literal_eval
import version
import tkinter
from tkinter import filedialog
from win10toast_click import ToastNotifier

user = os.getlogin()

while True:

    MYDIR = "C:/Users/" + user + "/alpha67_MP"
    CHECK_FOLDER = os.path.isdir(MYDIR)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory("alpha67_MP", "C:/Users/" + user)
        createDirectory("mods", "C:/Users/" + user + "/alpha67_MP")
        break

    else:
        update = version.needUpdate()
        needGetJsonAdress = True

    def needUpdateJson():

        user = os.getlogin()

        data = """{ok: salut}"""
        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["tag_name"]

        da = date.today()
        now = datetime.now()

        try:
            f = open('C:/Users/' + user + '/alpha67_MP/data.json')

            with open('C:/Users/' + user + '/alpha67_MP/data.json', 'r') as json_file:
                uInfo = json.load(json_file)
                uInfo = literal_eval(uInfo)
                uInfo = uInfo["version"]
            if uInfo != data:
                return True
            else:
                return False
            # Do something with the file
        except IOError:
            with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w') as outfile:
                json.dump(str({"time": str(now), "version": None}), outfile)
            print("File not accessible, starting his creation")
            return True

    up = needUpdateJson()

    if up == True:
        print("intallation de la mise à jour")
        user = os.getlogin()

        with open('C:/Users/' + user + '/alpha67_MP/data.json', 'r') as file:
            uInfo = json.load(file)
            uInfo = literal_eval(uInfo)
            adress = uInfo['path']


        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["assets"]
        data = data[0]
        url = data["browser_download_url"]

        urllib.request.urlretrieve(url, "C:/Users/" + user + "/alpha67_MP/mods/mp.zip")

        original = r'C:/Users/' + user + '/alpha67_MP/mp.zip'
        target = adress + "/ModPack.zip"

        # shutil.copyfile(original, target)

        from zipfile import ZipFile

        with ZipFile('C:/Users/' + user + '/alpha67_MP/mods/mp.zip', 'r') as zip:
            zip.printdir()
            zip.extractall(adress)

        now = datetime.now()

        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["tag_name"]
        print(data)

        with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w+') as outfile:
            json.dump(str({"time": str(now), "version": data, "path": adress}), outfile)

    time.sleep(5)

