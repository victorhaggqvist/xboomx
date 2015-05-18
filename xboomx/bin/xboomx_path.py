#!/usr/bin/env python3
# coding=utf-8

import os
from xboomx.config import config

__author__ = 'Victor Häggqvist'

def main():
    paths = os.environ['PATH'].split(':')

    items = []

    for path in paths:
        if os.path.isdir(path):
            for f in os.listdir(path):
                items.append(f)

    unique_items = list(set(items))

    ignore_list = config.get("ignorelist", "")
    for item in unique_items:
        if item not in ignore_list:
            print(item)

if __name__ == '__main__':
    main()
