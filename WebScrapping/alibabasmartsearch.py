#!python3
#smart search for alibaba products

import requests,webbrowser,bs4,sys

print('hold a sec...')
res = requests.get('https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText='+''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
links = soup.select('.h2 a')
print (len(links))

numopen=min(5,len(links))
for i in range (numopen):
    webbrowser.open('https://www.alibaba.com/product-detail/'+ links[i].get('href'))
