#!/usr/bin/python
import sys
import fileinput

import xboomx.db


def main():
    # get db type
    db_type = ''
    if len(sys.argv) > 1:
        db_type = sys.argv[1]
    # open db
    db = xboomx.db.open_shelve(db_type)

    # get item to update
    item = fileinput.input([]).next()
    item = item.strip('\n')

    # update item
    db[item] = db.get(item, 0) + 1

    # print it
    print item

    # clean up
    db.sync()
    db.close()


main()
