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
import win32com.client

user = os.getlogin()

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(r'C:\Users/'+ user +'/AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup/Updater.lnk')
shortcut.Targetpath = r"C:\Program Files\alpha67-downloader/Updater.exe"
shortcut.save()


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
        version = data["tag_name"]

        da = date.today()
        now = datetime.now()

        try:

            f = open("C:/Users/"+ user +"/AppData\Roaming/alphaProgram/version.txt", "r")
            txtVersion = f.read()

            if txtVersion != version:
                return True
            else:
                return False
            # Do something with the file
        except IOError:
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
    def checkAppVersionFile():
        try:
            f = open("C:/Users/"+ user +"/AppData\Roaming/alphaProgram/version.txt")
            return False
        except IOError:
            print("File not accessible")
            return True

    if checkBackground() == True or checkDownloader() == True or checkAppVersionFile() == True:
        updateProgram()
    else:
        print("all files are correctly install")

    if needUpdateJson() == True:
        updateProgram()
    else:
        print("you are up to date")


def updateProgram():

    print('starting update')

    user = os.getlogin()

    for files in os.listdir("C:/Users/"+ user +"/AppData\Roaming/alphaProgram"):
        if os.path.isfile(os.path.join("C:/Users/"+ user +"/AppData\Roaming/alphaProgram", files)):
            if '.exe' in files:
                print("exe file found")
                os.system("taskkill /im "+ files +" /f")


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

    print(url)

    urllib.request.urlretrieve(url, "C:/Users/"+user+"\AppData\Roaming/alphaProgram/app.zip")

    # shutil.copyfile(original, target)

    from zipfile import ZipFile
    with ZipFile("C:/Users/"+user+"\AppData\Roaming/alphaProgram/app.zip", 'r') as zip:
        zip.printdir()
        zip.extractall("C:/Users/"+user+"\AppData\Roaming/alphaProgram/")

    response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/alpha67-downloader/releases")
    data = json.loads(response.read())
    data = data[0]
    version1 = data["tag_name"]

    f = open("C:/Users/"+ user +"/AppData\Roaming/alphaProgram/version.txt", "w")
    f.write(str(version1))
    f.close()

    toaster = ToastNotifier()

    # showcase
    toaster.show_toast(
        "Alpha67 ",  # title
        "Une nouvelle version de Alpha67 downloader viens d'être installer.",  # message
        icon_path="icon.ico",  # 'icon_path'
        duration=5,
        # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True,
        # True = run other code in parallel; False = code execution will wait till notification disappears
        callback_on_click=None  # click notification to run function
    )



while True:
    start()
    time.sleep(30)







