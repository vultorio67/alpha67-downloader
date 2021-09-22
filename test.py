from tabulate import tabulate
import os
import json
from ast import literal_eval
import time
import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

import webbrowser
from win10toast_click import ToastNotifier

# function
page_url = 'http://example.com/'

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
    )