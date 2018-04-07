#! /usr/bin/env python3

#pw.py an insecure password vault

myshit = {  'email':'pussyslayer69',
            'facebook': 'asjdosdufsi',
            'myspace':'garbage1234'}
import sys,pyperclip

if len(sys.argv)<2:
    print('To use this scrip, type #py.py+[account]-to copy account password')
    sys.exit()

account = sys.argv[1]  #reminder argv[0] = pw.py/ argv[1] = account

if account in myshit:
    pyperclip.copy(myshit[account])
    print('password from '+account+'copied to clipboard')
else:
    print('there is no such account')
