from bs4 import BeautifulSoup as bs
import os,sys,requests

term='paris'
url = 'https://www.google.com/search?q='+term+'&source=lnms&tbm=isch'
path = '/Users/bentolima/Pictures/googlescrapping'

os.makedirs(path, exist_ok=True)

while (True):
    print('Downloading images...')
    res=requests.get(url)
    res.raise_for_status()
    soup=bs(res.text,'html.parser')

    #linkimg= soup.select('div img')
    for link in soup.find_all('a'):
        print(link.get('img'))
