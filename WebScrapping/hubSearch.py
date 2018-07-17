#!python3

import bs4,requests,webbrowser,sys
from bs4 import BeautifulSoup

print('Downloading page...')

res = requests.get('https://www.xvideos.com/?k='+' '.join(sys.argv[1:]))
res.raise_for_status()

soup = BeautifulSoup(res.text)
links = soup.select('p > a')

print(links[1].attrs)

numopen = min(len(links),4)

for i in range (numopen):
    webbrowser.open('https://www.xvideos.com'+links[i].get('href'))
