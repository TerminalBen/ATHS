
#! /usr/bin/env python3.
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#		 py.exe mcb.pyw delete <keyword> - deletes keyword from shelf
#		 py.exe mcb.pyw dall - deletes all keywords from shelf



import shelve, pyperclip, sys

mcbshelve = shelve.open('mcb')

#save clipboard content


if len(sys.argv) == 3:							#saves from clipboard do shelf
	if sys.argv[1].lower() == 'save': 
		mcbshelve[sys.argv[2]] = pyperclip.paste()
	if sys.argv[1].lower() ==	'delete':		#delete from shelve
		if sys.argv[2] in shelve.keys():
			del mcbshelve[sys.argv[2]] 	
	
elif  len(sys.argv) == 2:
	if sys.argv[1].lower == 'list':				#loads all keywords from shelf
		pyperclip.copy(str(list(mcbshelve.keys())))
	
	if sys.argv[1].lower() == 'dall':				#deletes all keys from shelf
		for key in list(mcbshelve.keys()):
			del mcbshelve[key]	

	elif sys.argv[1] in shelve:
		pyperclip.copy(mcbshelve[sys.argv[1]])


mcbshelve.close()