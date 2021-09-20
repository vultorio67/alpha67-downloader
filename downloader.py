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

def createDirectory(name, parent):
    path = parent+"/"+name
    print(path)
    isdir = os.path.isdir(path)
    print(isdir)
    if isdir == False:

        directory = name
        parent_dir = parent
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Directory '% s' created" % directory)

def get():
    tkinter.Tk().withdraw()
    user = os.getlogin()
    folder_path = dirName = filedialog.askdirectory(initialdir="C:/Users/"+user+"/AppData/Roaming/.minecraft", title='Please select a directory')
    return folder_path


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


print(url)

print("SVP veuillez renseigner où est votre dossier mods minecraft.")

time.sleep(2)

adress = get()

print("démarrage du téléchargement.")

print(adress)

user = os.getlogin()

createDirectory("alpha67_MP", "C:/Users/"+user)

createDirectory("mods", "C:/Users/"+user+"/alpha67_MP")


#urllib.request.urlretrieve(url, "C:/Users/"+user+"/alpha67_MP/mods/mp.zip")

original = r'C:/Users/'+user+'/alpha67_MP/mp.zip'
target = adress+"/ModPack.zip"

#shutil.copyfile(original, target)

import zipfile
with ZipFile('C:/Users/'+user+'/alpha67_MP/mp.zip', 'r') as zip:
    zip.printdir()
    zip.extractall() 