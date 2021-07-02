#!/usr/bin/python3

import re

fstRegex = re.compile(r'[a-z]')
secRegex = re.compile(r'[A-Z]')
thrRegex = re.compile(r'[0-9]')

text = input()
mo1 = fstRegex.search(text)
mo2 = secRegex.search(text)
mo3 = thrRegex.search(text)

if len(text) > 8:
    if mo1 != None and mo2 != None and mo3 != None:
        print('strong key!')
    else:
        print('bad key, must include upper and lower and digits, and longer than 8 characters!')
else:
    print('bad key, must include upper and lower and digits, and longer than 8 characters!')
