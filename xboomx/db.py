import shelve
import os


def open_shelve(db_type=''):
    # create dir if not exists
    try:
        os.makedirs(os.getenv("HOME") + '/.xboomx')
    except:
        pass

    # open shelve
    return shelve.open(os.getenv("HOME") + '/.xboomx/xboomx%s.db' % db_type)
