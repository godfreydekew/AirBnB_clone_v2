#!/usr/bin/python3
import sys
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

user = os.environ.get('HBNB_MYSQL_USER')
password = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
database = os.environ.get('HBNB_MYSQL_DB')

class DBStorage:
    """Defines the database class"""
    __engine = None
    __session = None
    def __init__(self):
        DBStorage.__engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(user, password, database), pool_pre_ping=True)
        Base.metadata.create_all(DBStorage.__engine)
        Session = sessionmaker(bind=DBStorage.__engine)
        DBStorage.__session = Session()
    def all(self, cls=None):
        """Returns all objects in the"""
        if cls is None:
            return self.__session.query(Base).all()
        else:
            return self.__session.query(cls).all()
    
    def new(self, obj):
        """Adds new object to database"""
        self.__session.add(obj)
    def save(self):
        """Saves changes to database"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Deletes object from database"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Reloads database"""
        Base.metadata.drop_all(DBStorage.__engine)
        Base.metadata.create_all(DBStorage.__engine)
        session_factory= sessionmaker(bind=DBStorage.__engine,  expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()
