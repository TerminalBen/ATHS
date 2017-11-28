
#! /usr/bin/env python3.
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.



import shelve, pyperclip, sys

mcbshelve = shelve.open('mcb')

#save clipboard content


if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbshelve[sys.argv[2]] = pyperclip.paste()
#list keywords and load contents
	
elif  len(sys.argv) == 2:
	if sys.argv[1].lower == 'list':
		pyperclip.copy(str(list(mcbshelve.keys())))
	elif sys.argv[1] in shelve:
		pyperclip.copy(mcbshelve[sys.argv[1]])
















mcbshelve.close()