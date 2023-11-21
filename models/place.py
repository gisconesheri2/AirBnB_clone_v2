#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    def __init__(self, **kwargs):
        """initialize the child class"""
        BaseModel.__init__(self)
        BaseModel.__init__(self, **kwargs)

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float())
    longitude = Column(Float())
    amenity_ids = []

    reviews = relationship('Place', backref='place', cascade='all, delete')
    amenities = relationship('Amenity', secondary='place_amenity',
                             backref='place_amenities', viewonly=False)

    @property
    def reviews(self):
        """defines the relationship between a place object
        and its reviews in File storage"""
        from models.__init__ import storage
        related_reviews = []
        file_reviews = storage.all('Review')
        for key, value in file_reviews.items():
            if value.place_id == self.id:
                related_reviews.append(value)
        return related_reviews

    @property
    def amenities(self):
        """return amenity instances of the amenity_ids
        list of the amenities linked to place"""
        from models.__init__ import storage
        amenities = storage.all('Amenity')
        amenity_instances = []
        for amenity_id in self.amenity_ids:
            key = f'Amenity.{amenity_id}'
            try:
                amenity_instances.append(amenities[key])
            except KeyError:
                pass
        return amenity_instances

    @amenities.setter
    def amenities(self, obj):
        """adds @obj's id to the amenity_ids list
        if it is an Amenity object"""
        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)
