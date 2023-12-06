#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """This class manages storage of hbnb models in mysql format"""
    __engine = None
    __session = None

    def __init__(self):
        '''create the engine, engine linked to the MySQL database and user'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Show all the objects or a specific group'''
        list_objs = []
        if cls is None:
            # list_objs += self.__session.query(User).all()
            list_objs += self.__session.query(State).all()
            list_objs += self.__session.query(City).all()
            # list_objs += self.__session.query(Amenity).all()
            # list_objs += self.__session.query(Place).all()
            # list_objs += self.__session.query(Review).all()
        else:
            list_objs = self.__session.query(cls).all()
        dict_objs = {}
        for obj in list_objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dict_objs[key] = obj
            # dict_objs[obj.__class__.__name__ + "." + obj.id](obj)
        return dict_objs

    def new(self, obj):
        '''add the object to the current database'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database'''
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
