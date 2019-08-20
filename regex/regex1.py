#! python3

#phone and email txt extractor

import pyperclip, re

phoneregex = re.compile(r'((\+)?)((\d{3}|\(\d{3}\))?)((\s|-)?)(\d{3})(\s?\d{2})(\s?\d{2})')
                            #comment this
emailregex = re.compile (r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+(\.[a-zA-z]{2,4}))')
                            #anything (1 or+) @ anything(1 or+) dot 2or 4 letters
dateRegex = re.compile (r'((\d{1,31})(\.|\\|\/|\-)(\d{1,12})(\.|\\|\/|\-)\d{4})')
                            #1-31 ./\- 1-12 ./\- dddd

input = str(pyperclip.paste())
matches = []

for group in phoneregex.findall(input):
    phonenum = '-'.join(group[1],group[2],group[3])
    matches.append(phonenum)
for group in emailregex.findall(input):
    matches.append(group[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('there are no records to be copied.')
