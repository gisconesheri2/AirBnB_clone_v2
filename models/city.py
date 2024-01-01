#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    def __init__(self, **kwargs):
        """initialize the child class"""
        BaseModel.__init__(self)
        BaseModel.__init__(self, **kwargs)

    __tablename__ = 'cities'

    state_id = Column(String(60, collation='latin1_swedish_ci'), ForeignKey('states.id'), nullable=False)
    name = Column(String(128, collation='latin1_swedish_ci'), nullable=False)

    places = relationship('Place', backref='cities', cascade='all, delete')
