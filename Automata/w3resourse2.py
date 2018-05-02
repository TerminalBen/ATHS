#!python3

import re

regex1 = re.compile(r'[a-z]+[A-Z]+[0-9]+')
regex2 = re.compile(r'a{1}b*')
regex3 = re.compile(r'a{1}b+.*')
regex4 = re.compile(r'a{1}b{0,1}')
regex7 = re.compile(r'[a-z]+_[a-z]+$')
regex8 = re.compile(r'[A-Z][a-z]+')
regex10 = re.compile(r'\w+')
regex11 = re.compile(r'\w\S$')
regex17 = re.compile(r'.*[0-9]$')


ip = "216.08.094.196"

def textmatch(text):
    if re.search(regex4,text):
        return('found  a match')
    else:
        return ('not matched')
print(textmatch('ab'))


def rem_ip(text):
    new = re.sub('\.[0]*','.', text)
    return new
print (rem_ip(ip))
