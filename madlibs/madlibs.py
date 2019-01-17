


import sys, shelve

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