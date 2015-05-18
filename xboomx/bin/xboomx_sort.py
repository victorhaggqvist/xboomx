#!/usr/bin/env python3
import fileinput

from xboomx.sqlitemgr import get_session, PathItem


def main():
    session = get_session()
    dbitems = session.query(PathItem).all()

    items = {}
    for i in dbitems:
        items[i.name] = i.count

    # read lines and set weight according to db
    items = []
    for input_item in fileinput.input([]):
        input_item = input_item.strip('\n')

        try:
            count = items[input_item]
            items.append((count, input_item))
        except KeyError:
            items.append((0, input_item))

    # sort items
    items.sort(key=lambda x: x[0], reverse=True)

    # print items to be shown on dmenu
    for item in items:
        print(item[1])

    session.close()


if __name__ == '__main__':
    main()
