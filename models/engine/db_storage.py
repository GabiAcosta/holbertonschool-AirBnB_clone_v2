#!/usr/bin/python3
"""
This module defines a class to manage storage
from the database for the hbnb clone
"""
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Create an instance of the storage
        database to create the engine
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB"),
                                             pool_pre_ping=True))

        if getenv("HBNB_ENV ") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query about the current database session
        """
        dic_of_objects = {}
        if cls and cls in classes.values():
            all_objetcs = self.__session.query(cls).all()
            for obj in all_objetcs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                value = obj
                dic_of_objects[key] = value
        elif cls is None:
            for cls in classes.values():
                all_objetcs = self.__session.query(cls).all()
                for obj in all_objetcs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    value = obj
                    dic_of_objects[key] = value
        return dic_of_objects

    def new(self, obj):
        """
        Method to add the object to the
        current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Method to commit all changes to the
        current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Method to remove from
        current database session obj if not None
        """
        if obj:
            self.__session.delete((obj))

    def reload(self):
        """
        create all tables in database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        call the remove() method on the private session attribute
        """
        self.__session.close()