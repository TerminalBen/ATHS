import re

madlibs = open ('...\madlibs.txt') # fix path
content = madlibs.read()           #save Txt content
check = re.compile(r'Adjective|Verb|Noun|Adverb') #regexs 'O'

while True:                             #infinite loop
    result = check.search(content)          #tore results of regex earch in variable

    if result == None:                  #if no maches found, end
        break

    elif result.group() == 'Adjective' or result.group() == 'Verb' or # looking for the regexes in the groups formed (nasty)
            result.group() == 'Noun' or result.group() == 'Adverb'
        print (('enter a %s 'result.group().lower()))                      # print a string (found regex)
        i = input()

        content = check.sub(i,content,1)                    #replace the content for  input once using regex.sub
print content                                               #print  content

print ('Name your File:')
name = input()
newFile = open('.../ %s.txt', % (name),'w')                 #newfile at path with input name  writing  conditions
newFile.write(content)                                      #write content to newFile
newFile.close()                                             #procedual close
