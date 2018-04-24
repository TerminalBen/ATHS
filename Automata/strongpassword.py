#!python3

#strong password detection
import re

strongregex1 = re.compile(r'[a-zA-Z0-9]*[[a-zA-Z0-9]+') #takes everything
strongregex2 = re.compile(r'[a-z]+[A-Z]+\d+') #demands order

strongalfa = re.compile(r'[A-Z]+') #regex for alfa characters, For minor characters and for digits
strongminor = re.compile(r'[a-z]+')
strongdigit = re.compile(r'\d+')

def chechpass(text):#return true if text has all of the regexes and if length is >8. to be used in assertions
    return bool (strongalfa.search(text) and strongminor.search(text) and
                    strongdigit.search(text) and len(text)>=8)

#mypass = ('1Aa')

assert chechpass('1aA') is False
assert chechpass('abc!@#123ABC<>/.,{}\\|') is True
assert chechpass('abc123ABC') is True
assert chechpass('aA1') is False
assert chechpass('!@#$%^&*(') is False
assert chechpass('<A<b<2<<') is True
assert chechpass('x1y2z3TT') is True
