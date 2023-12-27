#!/usr/bin/python3
"""
engine to interact with a database storage model
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBStorage():
    """model to comuunicate with the underlying database"""

    __engine = None
    __session = None

    def __init__(self):
        """get the necessary env variables from os.environ
        and create the engine that connects to the database"""
        user = os.environ['HBNB_MYSQL_USER']
        password = os.environ['HBNB_MYSQL_PWD']
        host = os.environ['HBNB_MYSQL_HOST']
        database = os.environ['HBNB_MYSQL_DB']
        program_env = os.environ['HBNB_ENV']

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if program_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of ojcets of @cls in the database
        or every object present"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        result_dict = {}
        if cls is not None:
            if type(cls) is str:
                results = self.__session.query(classes[cls])
            else:
                results = self.__session.query(cls)
        else:
            results = self.__session.query(State,
                                           City)

        for result in results:
            key = f'{result.__class__.__name__}.{result.id}'
            result_dict[key] = result

        return result_dict

    def new(self, obj):
        """adds a newly created object to the session object"""
        self.__session.add(obj)

    def save(self):
        """commits the changes to the database permanently"""
        self.__session.commit()

    def delete(self, obj):
        """deletes the @obj from the session object"""
        if obj is not None:
            classes = {
                        'BaseModel': BaseModel, 'User': User, 'Place': Place,
                        'State': State, 'City': City, 'Amenity': Amenity,
                        'Review': Review
                      }
            key = result.__class__.__name__
            i = self.__session.query(classes[key])\
                    .filter(classes[key].id == obj.id).one()
            session.delete(i)

    def reload(self):
        """create all tables in the database and start up the session object"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from sqlalchemy.orm import scoped_session, sessionmaker

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """calls remove on the current scoped session
        essentially closing the session
        """
        self.__session.close()

