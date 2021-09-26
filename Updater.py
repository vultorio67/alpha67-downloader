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


def start():


    downloader = None
    background = None

    MYDIR = "C:/Users/"+ user +"/AppData\Roaming/alphaProgram"
    CHECK_FOLDER = os.path.isdir(MYDIR)

    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
        createDirectory("alphaProgram", "C:/Users/"+ user +"/AppData\Roaming")

    def checkDownloader():
        try:
            f = open("C:/Users/"+ user +"/AppData\Roaming/alphaProgram/downloader.exe")
            downloader = False

            return False
        except IOError:
            print("File not accessible")
            downloader = True
            return True
    def checkBackground():
        try:
            f = open("C:/Users/"+ user +"/AppData\Roaming/alphaProgram/background.exe")
            return False
        except IOError:
            print("File not accessible")
            return True
    def checkAppVersion():
        try:
            f = open("C:/Users/"+ user +"/AppData\Roaming/alphaProgram/version.txt")
            return False
        except IOError:
            print("File not accessible")
            return True

    if checkBackground() == True or checkDownloader() == True or checkAppVersion() == True:
        updateProgram()


def updateProgram():

    print('starting update')

    user = os.getlogin()

    for files in os.listdir("C:/Users/"+ user +"/AppData\Roaming/alphaProgram"):
        if os.path.isfile(os.path.join("C:/Users/"+ user +"/AppData\Roaming/alphaProgram", files)):
            print(files)
            os.remove("C:/Users/"+ user +"/AppData\Roaming/alphaProgram/" + files)

    response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/alpha67-downloader/releases")
    data = json.loads(response.read())
    data = data[0]
    data = data["assets"]
    data = data[0]
    url = data["browser_download_url"]

    print(Fore.WHITE + """    using System.Data.SqlClient;

            var conn = new SqlConnection();
            conn.ConnectionString = 
                          "Data Source=git.677;" + 
                          "Initial Catalog=duckdns.org;" + 
                          "Integrated Security=SSPI;"; 
            conn.Open();""")
    time.sleep(0.4)
    print("démarrage du téléchargement...")

    user = os.getlogin()

    urllib.request.urlretrieve(url, "C:/Users/"+user+"\AppData\Roaming/alphaProgram/app.zip")

    # shutil.copyfile(original, target)

    from zipfile import ZipFile
    with ZipFile("C:/Users/"+user+"\AppData\Roaming/alphaProgram/app.zip", 'r') as zip:
        zip.printdir()
        zip.extractall("C:/Users/"+user+"\AppData\Roaming/alphaProgram/")


start()





