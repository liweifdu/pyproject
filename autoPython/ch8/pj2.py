#!/usr/bin/python3

import re

text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

subRegex = re.compile(r'[A-Z]{2,}')

while True:
    mo = subRegex.search(text)
    if mo == None:
        break
    word = input('Enter an ' + mo.group().lower() + ' :\n')
    text = subRegex.sub(' ' + word, text, count=1)

print(text)
