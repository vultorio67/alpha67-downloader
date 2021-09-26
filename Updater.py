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
import glob
import pydirectory
import win32com.client

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



def createDirectory(name, parent):
    path = parent+"/"+name
    isdir = os.path.isdir(path)
    if isdir == False:

        directory = name
        parent_dir = parent
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Directory '% s' created" % directory)

def needUpdateJson():

        user = os.getlogin()

        data = """{ok: salut}"""
        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/alpha67-downloader/releases")
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

def checkMpUpdate():

    user = os.getlogin()

    MYDIR = "C:/Users/" + user + "/alpha67_MP"
    CHECK_FOLDER = os.path.isdir(MYDIR)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory("alpha67_MP", "C:/Users/" + user)l*
        createDirectory("mods", "C:/Users/" + user + "/alpha67_MP")


    else:
        update = version.needUpdate()
        needGetJsonAdress = True

    up = needUpdateJson()

    if up == True:

        now = datetime.now()

        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/alpha67-downloader/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["tag_name"]

        with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w') as outfile:
            json.dump(str({"time": str(now), "version": data}), outfile)

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

        toaster = ToastNotifier()

        # showcase
        toaster.show_toast(
            "Alpha67 ",  # title
            "Une nouvelle version du modpack viens d'être installer.",  # message
            icon_path="icon.ico",  # 'icon_path'
            duration=5,
            # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True,
            # True = run other code in parallel; False = code execution will wait till notification disappears
            callback_on_click=None  # click notification to run function
        )

        now = datetime.now()

        response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
        data = json.loads(response.read())
        data = data[0]
        data = data["tag_name"]
        print(data)

        with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w+') as outfile:
            json.dump(str({"time": str(now), "version": data, "path": adress}), outfile)



while True:
    checkMpUpdate()

    time.sleep(120)





