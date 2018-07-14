#!python3
#automatic google search from command line

import requests, webbrowser,bs4,sys


#Downloading the page
print ('Googling...please wait')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#retrieve top search result links
soup = bs4.BeautifulSoup(res.text)
links = soup.select('.r a')
print (len(links))

#open webbrowser for each search
numopen=min(5,len(links))
for i in range (numopen):
    webbrowser.open('http://google.com'+ links[i].get('href'))
