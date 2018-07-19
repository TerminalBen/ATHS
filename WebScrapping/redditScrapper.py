#!python3
#Download reddit links to file

import bs4,requests, os
from bs4 import BeautifulSoup


pagefile= requests.get('https://reddit.com')
pagefile.raise_for_status()
soup = BeautifulSoup(pagefile.text,'html.parser')
sall = soup.select('p  a')

file= open('redditLinks.txt','a')

for href in sall:
    file.write(str(href))

file.close()
