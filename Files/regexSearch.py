import os,re

matches = []
path = '/Users/bentolima/Documents/Projects/ATHS/Files'
regex = re.compile (r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+(\.[a-zA-z]{2,4}))')

for filename in os.listdir(path):                   #iterate files
    if filename.endswith('.txt'):                   #only .txt files
        for i,line in enumerate(open(filename)):    #iterate lines
            for match in re.finditer(regex,line):    #search matches
                matches.append(match.groups())      #append matches to array

print (matches)
