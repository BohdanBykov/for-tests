
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql


# create engine
engine = sqlalchemy.create_engine('mysql+pymysql://test:password@127.0.0.1/testdb', echo=True)

base = declarative_base()

class User(base):
    __tablename__ = 'user'

    user_id = Column(Integer, auto_increment=True, primary_key=True)
    firstname = Column(String(200))

    def __init__(self, user_id, firstname):
        self.user_id = user_id
        self.firstname = firstname

base.metadata.create_all(engine)
