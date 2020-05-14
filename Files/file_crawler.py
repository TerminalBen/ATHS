#find word in s txt file in a folder

import os
import glob

for filename in glob.glob('*.txt'):
    fileopen=open(filename,'r')
    data= fileopen.readlines()
    lst=str(data)
    for word in lst.split():
        if ('she' in word):
            print (word +' '+ filename)
