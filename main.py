import urllib.request
import downloader

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        downloader.main()
        return True
    except:
        return False


