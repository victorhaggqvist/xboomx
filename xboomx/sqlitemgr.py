# coding=utf-8
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

__author__ = 'Victor Häggqvist'

# create dir if not exists
try:
    os.makedirs(os.getenv("HOME") + '/.xboomx')
except:
    pass

dbname = 'xboomx_sqlite.db'
dbpath = os.path.join(os.getenv("HOME"), '.xboomx', dbname)
dsn = 'sqlite:///%s' % dbpath

engine = create_engine(dsn, echo=False)
Base = declarative_base()


class PathItem(Base):
    __tablename__ = 'pathitems'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count = Column(Integer)

    def __repr__(self):
        return "<PathItem(name='%s', count='%s')>" % (self.name, self.count)


def get_session():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
