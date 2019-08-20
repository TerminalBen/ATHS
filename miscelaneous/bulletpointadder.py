#!/usr/bin/env python3
# a bullet poin adder from and to clipboard

import sys,pyperclip

text = pyperclip.paste()

lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    lines[i] = '* '+lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
