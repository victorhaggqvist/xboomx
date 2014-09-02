#!/usr/bin/python

import os
from xboomx.config import config

def main():
    pathes = os.environ['PATH'].split(':')

    items = []

    for path in pathes:
        if os.path.isdir(path):
            for f in os.listdir(path):
                items.append(f)

    uniqeitems = list(set(items))

    ignorelist = config.get("ignorelist","");
    for item in uniqeitems:
        if item not in ignorelist:
            print item

main()