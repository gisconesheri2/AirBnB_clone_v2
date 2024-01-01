#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = "reviews"

    def __init__(self, **kwargs):
        """initialize the child class"""
        BaseModel.__init__(self)
        BaseModel.__init__(self, **kwargs)

    text = Column(String(1024, collation='latin1_swedish_ci'), nullable=False)
    place_id = Column(String(60, collation='latin1_swedish_ci'), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60, collation='latin1_swedish_ci'), ForeignKey('users.id'), nullable=False)
