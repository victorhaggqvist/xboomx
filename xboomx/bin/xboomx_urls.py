#!/usr/bin/python

import xboomx.db
DB_TYPE = 'urls'


def main():
    db = xboomx.db.open_shelve(DB_TYPE)
    for url in db.keys():
        print url

    db.close()


main()
