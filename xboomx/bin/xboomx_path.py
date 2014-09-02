#!/usr/bin/python

import os

pathes = os.environ['PATH'].split(':')


for path in pathes:
    if os.path.isdir(path):
        for f in os.listdir(path):
            print f
