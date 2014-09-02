#!/usr/bin/python
import fileinput
import sys

import xboomx.db


def main():

    # get db type
    db_type = ''
    if len(sys.argv) > 1:
        db_type = sys.argv[1]

    # open shelve
    db = xboomx.db.open_shelve(db_type)

    # read lines and set weight according to db
    items = []

    for input_item in fileinput.input([]):
        input_item = input_item.strip('\n')
        items.append((db.get(input_item, 0), input_item))

    # sort items
    items.sort(key=lambda x: x[0], reverse=True)

    # print items
    for item in items:
        print item[1]

    # clean up
    db.close()


main()
