import re
import json
import urllib
import urllib.request
import time
import tkinter
from tkinter import filedialog
import os
import os.path
import shutil
from colorama import Fore, Back, Style
from datetime import date, datetime
from ast import literal_eval
import version
from tabulate import tabulate
import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

import webbrowser
from win10toast_click import ToastNotifier



user = os.getlogin()

def get():
    print(Back.WHITE + Fore.BLACK + "SVP veuillez renseigner où est votre dossier mods minecraft.")
    tkinter.Tk().withdraw()
    user = os.getlogin()
    folder_path = dirName = filedialog.askdirectory(initialdir="C:/Users/"+user+"/AppData/Roaming/.minecraft", title='Please select a directory')
    return folder_path

time.sleep(2)

def createDirectory(name, parent):
    path = parent+"/"+name
    isdir = os.path.isdir(path)
    if isdir == False:

        directory = name
        parent_dir = parent
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Directory '% s' created" % directory)

MYDIR = "C:/Users/" + user + "/alpha67_MP"
CHECK_FOLDER = os.path.isdir(MYDIR)
# If folder doesn't exist, then create it.
if not CHECK_FOLDER:
    os.makedirs(MYDIR)
    print("created folder : ", MYDIR)
    createDirectory("alpha67_MP", "C:/Users/" + user)
    createDirectory("mods", "C:/Users/" + user + "/alpha67_MP")
    update = True
    adress = get()
    needGetJsonAdress = False

else:
    update = version.needUpdate()
    needGetJsonAdress = True

if update == True:

    infoFile = 'C:/Users/' + user + '/alpha67_MP/data.json'

    if needGetJsonAdress == True:
        with open(infoFile, 'r') as file:
            uInfo = json.load(file)
            uInfo = literal_eval(uInfo)
            adress = uInfo['path']
    try:
        None
    except:
        print("sorry but the program can't connect to internet")
    response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
    data = json.loads(response.read())
    data = data[0]
    data = data["assets"]
    data = data[0]
    url = data["browser_download_url"]



    print(Back.WHITE+Fore.BLACK+"Nous allons installer les mods dans ce repèrtoir : "+adress)
    time.sleep(1)
    print(Back.BLACK+Fore.WHITE+"connection au server")
    time.sleep(0.5)
    print(Fore.WHITE+"""    using System.Data.SqlClient;
    
        var conn = new SqlConnection();
        conn.ConnectionString = 
                      "Data Source=git.677;" + 
                      "Initial Catalog=duckdns.org;" + 
                      "Integrated Security=SSPI;"; 
        conn.Open();""")
    time.sleep(0.4)
    print("démarrage du téléchargement...")


    user = os.getlogin()



    urllib.request.urlretrieve(url, "C:/Users/"+user+"/alpha67_MP/mods/mp.zip")

    original = r'C:/Users/'+user+'/alpha67_MP/mp.zip'
    target = adress+"/ModPack.zip"

    #shutil.copyfile(original, target)

    from zipfile import ZipFile
    with ZipFile('C:/Users/'+user+'/alpha67_MP/mods/mp.zip', 'r') as zip:
        zip.printdir()
        zip.extractall(adress)

    user = os.getlogin()
    data = """{ok: salut}"""
    response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
    data = json.loads(response.read())
    data = data[0]
    data = data["tag_name"]
    print(data)

    da = date.today()
    now = datetime.now()
    print(da)

    with open('C:/Users/' + user + '/alpha67_MP/ListMods.txt', 'w') as f:
        f.write('')

    with open('C:/Users/' + user + '/alpha67_MP/ListMods.txt', 'a') as f:
        for files in os.listdir(adress):
            if os.path.isfile(os.path.join(adress, files)):
                print(files)
                f.write(files+"\n")

    with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w') as outfile:
        json.dump(str({"time": str(now), "version": data, "path": adress}), outfile)


    for i in range(100):
        print(Fore.GREEN+"unziping file "+str(i)+"%, directory get")
        time.sleep(0.005)

    with open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'w') as f:
        f.write('')
    me = ""
    with open('C:/Users/' + user + '/alpha67_MP/listMod.txt', 'a') as f:
        for files in os.listdir(adress):
            if os.path.isfile(os.path.join(adress, files)):
                f.write(files)
                print(files)
                me = me + "[ "+files+" ]"
                me = me

    x = me.split(" ")
    print(tabulate([[x]], headers=['Name', 'Age']))

    print(":::::Le modpack est correctement installer.")

    time.sleep(4)

else:
    print(Fore.GREEN+"vous êtes à jour.")
    toaster = ToastNotifier()

    # showcase
    toaster.show_toast(
        "Alpha67 : Votre modpack est à jour",  # title
        "cool",  # message
        icon_path="icon.ico",  # 'icon_path'
        duration=5,  # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True,
        # True = run other code in parallel; False = code execution will wait till notification disappears
        callback_on_click=open_url  # click notification to run function
    )

    time.sleep(4)
"""except:
    now = datetime.now()
    print("error!!!!")
    print("une erreur inconue empêche le program d'installer le modpack ou de verifier une mise à jour. Verifier vorte connexion à internet.")
    with open('C:/Users/' + user + '/alpha67_MP/data.json', 'w') as outfile:
        json.dump(str({"time": str(now), "version": None}), outfile)"""