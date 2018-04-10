#! python3

#phone and email txt extractor

import pyperclip, re

phoneregex = re.compile(r'((\+)?)(\d{3}|\(\d{3}\))(\s|-)(\d{7})')
                            #+ 3 numbers or (3 numbers) separator (space or -) followed by 7 numbers
emailregex = re.compile (r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+(\.[a-zA-z]{2,4}))')
                            #anything (1 or+) @ anything(1 or+) dot 2or 4 letters
dateRegex = re.compile (r'((\d{1,31})(\.|\\|\/|\-)(\d{1,12})(\.|\\|\/|\-)\d{4})')
