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

MYDIR = "C:/Users/" + user + "/AppData\Roaming/alphaProgram/"
CHECK_FOLDER = os.path.isdir(MYDIR)

def notif():
    toaster = ToastNotifier()

    # showcase
    toaster.show_toast(
        "Alpha67 ",  # title
        "Une nouvelle version d'alpha67 downloader est en cour d'installation, le logiciel se lancera dans 0,5 minute",  # message
        icon_path="icon.ico",  # 'icon_path'
        duration=5,
        # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True,
        # True = run other code in parallel; False = code execution will wait till notification disappears
        callback_on_click=None  # click notification to run function
    )

if not CHECK_FOLDER:
    os.system('start updater.exe')
    notif()
    time.sleep(30)

    def checkDownloader():
        try:
            f = open("C:/Users/" + user + "/AppData\Roaming/alphaProgram/background.exe")
            print("ok")
        except IOError:
            print("File not accessible")
            os.system('start updater.exe')
            notif()
            time.sleep(30)
    def checkBackground():
        try:
            f = open("C:/Users/" + user + "/AppData\Roaming/alphaProgram/downloader.exe")
            print("ok")
        except IOError:
            print("File not accessible")
            os.system('start updater.exe')
            notif()
            time.sleep(30)

    checkBackground()
    checkDownloader()


os.system('start C:/Users\%username%\AppData\Roaming/alphaProgram\downloader.exe')