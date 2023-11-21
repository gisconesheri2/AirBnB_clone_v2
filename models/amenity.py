#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class Amenity(BaseModel, Base):
    """models different amenities"""

    def __init__(self, **kwargs):
        """initialize the child class"""
        BaseModel.__init__(self)
        BaseModel.__init__(self, **kwargs)

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
