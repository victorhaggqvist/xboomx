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
        score = db.get(input_item, 0)
        items.append((score, input_item))
    
    for key in db.keys():
        # check if any item (from previous queries) is not yet in items
        if not [item[1] for item in items if item[1] == key]:
            items.append((db[key], key))


    # sort items
    items.sort(key=lambda x: x[0], reverse=True)

    # print items
    for item in items:
        print item[1]

    # clean up
    db.close()


main()
