#!/usr/bin/env python3
from pprint import pprint
import sys
import fileinput
from sqlalchemy.orm.exc import NoResultFound
from xboomx.sqlitemgr import get_session, PathItem


def main():
    # get db type
    db_type = ''
    if len(sys.argv) > 1 and sys.argv[1] != "--stats":
        db_type = sys.argv[1]

    item = fileinput.input()[0]
    pprint(item)

    item = item.strip('\n')

    session = get_session()
    try:
        dbitem = session.query(PathItem).filter_by(name=item).one()
        dbitem.count = dbitem.count + 1
        session.add(dbitem)
    except NoResultFound:
        dbi = PathItem(name=item, couunt=0)
        session.add(dbi)

    session.commit()
    session.close()

    print(item)

if __name__ == '__main__':
    main()
