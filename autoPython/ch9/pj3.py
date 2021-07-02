#!/usr/bin/python3

import os
import shutil
import re

def fillGap(dir, prefix):
    if not os.path.exists(dir):
        print('Directory not exists:')
        return

    filenum = 0
    filelist = []
    for file in os.listdir(dir):
        if file.startswith(prefix):
            filenum += 1
            filelist.append(file)
    filelist.sort()

    print(filelist)
    for i in range(filenum):
        srcfile = os.path.join(dir, filelist[i])
        dstfile = os.path.join(dir, prefix + '%03d'%(i+1) + '.txt')
        if srcfile != dstfile:
            print(srcfile, dstfile)
            shutil.move(srcfile, dstfile)

fillGap('.', 'pj')
