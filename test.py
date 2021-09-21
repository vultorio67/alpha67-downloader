import os




def needUpdateJson():
	user = os.getlogin()

	createDirectory("alpha67_MP", "C:/Users/"+user)

	createDirectory("mods", "C:/Users/"+user+"/alpha67_MP")
	data = """{ok: salut}"""
	response = urllib.request.urlopen("https://api.github.com/repos/vultorio67/desktop-tutorial/releases")
	data = json.loads(response.read())
	data = data[0]
	data = data["tag_name"]


	da = date.today()
	now = datetime.now()

	try:
	    f = open('C:/Users/' + user + '/alpha67_MP/test.json')

	    print("File data is already create.")
	    time.sleep(0.5)
	    print("checking the current version.")

	    with open('C:/Users/' + user + '/alpha67_MP/test.json', 'r') as json_file:
	        uInfo = json.load(json_file)
	        uInfo = literal_eval(uInfo)
	        uInfo = uInfo["version"]
	    if uInfo != data:
	        return True
	    else:
	        return False
	    # Do something with the file
	except IOError:
	    with open('C:/Users/' + user + '/alpha67_MP/test.json', 'w') as outfile:
	        json.dump(str({"time": str(now), "version": None}), outfile)
	    print("File not accessible, starting his creation")
	    return True






def needUpdateJar():
	ok = ""

	path = r'C:/Users/Elève/AppData/Roaming/.minecraft/mods'

	def existFile():
		try:
			open('listMod.txt', 'r')
			return True
		except:

			return False

	if existFile() == False:
		with open('listMod.txt', 'w') as f:
		    f.write('')

	with open('listMod.txt') as f:
	    contents = f.readlines()
	    with open('listMod.txt', 'w') as f:
		    f.write('')
	    #print(contents)


	with open('listMod.txt', 'a') as f:
	 	for files in os.listdir(path):
		    if os.path.isfile(os.path.join(path, files)):
		        #print(files)
		        ok = ok+files
		        f.write(files)


	contents = contents[0]

	if contents == ok:
		return False
	else:
		return True

if needUpdateJar() == True:
	print("jar is modified")
if needUpdateJson() == True:
	print("json version not up to date.")
