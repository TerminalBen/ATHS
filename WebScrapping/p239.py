#download Romeo and juliet to file from ATBS Website


import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
file = open('romeo and juliet.txt','wb')
for line in res.iter_content(1000000):
    x=file.write(line)
print(x) #print the number of bytes writen in file
file.close()
