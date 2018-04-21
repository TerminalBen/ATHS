import re

madlibs = open ('...\madlibs.txt')
content = madlibs.read()
check = re.compile(r'Adjective|Verb|Noun|Adverb')

while True:
    result = check.search(content)

    if result == None:
        break

    else if result.group() == 'Adjective' or result.group() == 'Verb' or result.group() == 'Noun' or result.group() == 'Adverb'
        print ()('enter a %s 'result.group().lower()))
        i = input()

        content = check.sub(i,content,1)
print content

print ('Name your File:')
name = input()
newFile = open('.../ %s.txt', % (name),'w')
newFile.write(content)        
