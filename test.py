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
from win10toast import ToastNotifier
from win10toast import *

toast = ToastNotifier()
toast.show_toast( title="Notification", msg="Here comes the message", icon_path=None, duration=5, threaded=False, callback_on_click=None)

# function
"""page_url = 'http://example.com/'

def open_url():
    print("download")

# initialize
toaster = ToastNotifier()

# showcase
toaster.show_toast(
    "Alpha67 mise à jour disponible", # title
    "Clicker pour l'installater", # message
    icon_path="icon.ico", # 'icon_path'
    duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
    callback_on_click=open_url # click notification to run function
    )"""