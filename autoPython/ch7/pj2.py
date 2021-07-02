#!/usr/bin/python3

import re

def myStrip(myStr, myKey=''):
    if len(myKey) > 0:
        rmStr = '((^' + myKey +'+)' + '|' + '(' + myKey + '+$))'
        rmRegex = re.compile(rmStr)
        myStr = rmRegex.sub(r'', myStr)
    else:
        rmRegex = re.compile(r'((^\s+)|(\s+$))')
        myStr = rmRegex.sub(r'', myStr)
    print(myStr)

myStrip('   agasf   ')
myStrip('hhhafsdfasfhhhh', 'h')
