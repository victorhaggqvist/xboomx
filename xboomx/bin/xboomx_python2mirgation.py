#!/usr/bin/env python2
# coding=utf-8
import os
from pprint import pprint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__author__ = 'Victor Häggqvist'

import shelve

dbname = 'xboomx.db'
shelvepath = os.path.join(os.getenv("HOME"), '.xboomx', dbname)
db = shelve.open(shelvepath)
pprint(db)


dbname = 'xboomx_sqlite.db'
dbpath = os.path.join(os.getenv("HOME"), '.xboomx', dbname)
dsn = 'sqlite:///%s' % dbpath

engine = create_engine(dsn, echo=True)
Base = declarative_base()

from sqlalchemy import Column, Integer, String


class PathItem(Base):
    __tablename__ = 'pathitems'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count = Column(Integer)

    def __repr__(self):
        return "<PathItem(name='%s', count='%s')>" % (self.name, self.count)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for dbi in db:
    print('migrating %s: %s' % (dbi, db[dbi]))
    sqlitem = PathItem(name=dbi, count=db[dbi])
    session.add(sqlitem)

session.commit()
print('migration done')
