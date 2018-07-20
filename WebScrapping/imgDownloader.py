#!python3

import bs4,requests,os
form bs4 import BeautifulSoup

url = 'https://www.flickr.com/search/?text='+' '.join(sys.argv[1:])
path ='/Users/bentolima/Documents/scriptDownloads'

os.makedirs(path,exist_ok=True)

while True():
    print ('downloading content')
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'html.parser')

    pic = soup.select('div a')

    picurl = ''
