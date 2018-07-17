#!python3

import bs4,requests,os
from bs4 import BeautifulSoup

url = 'https://xkcd.com'
path = '/Users/bentolima/Documents/comics'
os.makedirs(path,exist_ok = True)

while not url.endswith('#'):
    print('Downloaing page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'html.parser')

    comicElem = soup.select('#comic img')    #or soup.select(div img)
    if (comicElem == []):
        print('commic not found \n')
    else:
        comicurl = 'https:'+comicElem[0].get('src')
        print('Downloading image... %s' % (comicurl))
        res = requests.get(comicurl)
        res.raise_for_status()
        imgFile = open(os.path.join(path,os.path.basename(comicurl)),'wb')

        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()

#getprevious link
prevLink = soup.select('a[rel="prev"]')[0]
url='https://xqcd.com'+prevLink.get('href')

print(done)
