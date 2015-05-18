#!/usr/bin/env python3
import fileinput
from xboomx.sqlitemgr import get_session, PathItem
from xboomx.config import config

def main():
    session = get_session()
    dbitems = session.query(PathItem).all()

    memitems = {}
    for i in dbitems:
        memitems[i.name] = i.count

    # read lines and set weight according to db
    items = []
    for input_item in fileinput.input([]):
        input_item = input_item.strip('\n')

        try:

            count = memitems[input_item]
            items.append((count, input_item))
        except KeyError:
            items.append((0, input_item))

    # sort items
    items.sort(key=lambda x: x[0], reverse=True)

    # complete commands
    complete_offpath = config.get('complete_offpath', False)
    if complete_offpath:
        for key in memitems:
            # check if any item (from previous queries) is not yet in items
            if not [item[1] for item in items if item[1] == key]:
                items.append((memitems[key], key))

    # print items to be shown on dmenu
    for item in items:
        print(item[1])

    session.close()


if __name__ == '__main__':
    main()
