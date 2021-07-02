#!/usr/bin/python3

import os
import sys
import shutil

def copy(suffix, src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)

    try:
        for dirpath, dirnames, filenames in os.walk(src):
            for filename in filenames:
                if filename.endswith('.'+suffix):
                    print(os.path.join(dirpath,filename))
                    shutil.copy(os.path.join(dirpath, filename), dst)
    except shutil.SameFileError:
        print("Finished copying file.")

# copy('py', '.', 'pyfiles')
