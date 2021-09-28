import os

user = os.getlogin()

for files in os.listdir("C:/Users/" + user + "/AppData\Roaming/alphaProgram"):
    if os.path.isfile(os.path.join("C:/Users/" + user + "/AppData\Roaming/alphaProgram", files)):
        print(files)
os.system("taskkill /im background.exe /f")