#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    def __init__(self, **kwargs):
        """initialize the child class"""
        BaseModel.__init__(self)
        BaseModel.__init__(self, **kwargs)

    email = Column(String(128, collation='latin1_swedish_ci'), nullable=False)
    password = Column(String(128, collation='latin1_swedish_ci'), nullable=False)
    first_name = Column(String(128, collation='latin1_swedish_ci'))
    last_name = Column(String(128, collation='latin1_swedish_ci'))

    places = relationship('Place', backref='user', cascade='all, delete')
    reviews = relationship('Review', backref='user', cascade='all, delete')
