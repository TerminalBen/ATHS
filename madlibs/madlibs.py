


import sys, shelve
'''
list = ['ADJECTIVE','NOUN','ADVERB','VERB']
newmadlib=[]
lib_file = open('/Users/bentolima/Documents/Projects/ATHS/Madlibs/madlib.txt','r')


for word ,index in enumerate (lib_file.split()):
	if word.lower()in list:
		newmadlib[index] = input("enter a "+word.upper())

newmadlib = ' '.join(newmadlib)

print (lib_file)
print (newmadlib)
'''

PARTS_OF_SPEECH = ["verb", "noun", "adjective"]
with open('/Users/bentolima/Documents/Projects/ATHS/Madlibs/madlib.txt') as madLibFileObject:
     madLib = madLibFileObject.read()
newMadLib = []
for word, index in enumerate(madLib.split()):
     if word.lower() in PARTS_OF_SPEECH:
        newMadLib[index] = input("Enter " + word.upper())
newMadLib = ' '.join(newMadLib)
print(madLib)
print(newMadLib)