#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Table, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv
import models


place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
                          extend_existing=True)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='delete', backref='place')
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """ Getter of reviews """
            reviews = models.storage.all(Review)
            list_reviews = []
            for r in reviews.values():
                if self.id == r.place_id:
                    list_reviews.append(r)
            return list_reviews

        @property
        def amenities(self):
            """Getter of amenities """
            return [ame for ame in models.storage.all(Amenity).values()
                    if ame.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            """Setter of 1 amenity """
            if type(amenity) == Amenity:
                self.amenity_ids.append(amenity.id)
    # @property
    # def amenities(self):
    #     """Getter attribute that returns the list of Amenity instances."""
    #     amenities_list = []
    #     all_amenities = models.storage.all(Amenity)
    #     for amenity in all_amenities.values():
    #         if amenity.id in self.amenity_ids:
    #             amenities_list.append(amenity)
    #     return amenities_list

    # @amenities.setter
    # def amenities(self, amenity_obj):
    #     """Setter attribute that handles append method for adding an Amenity.id to amenity_ids."""
    #     if isinstance(amenity_obj, Amenity):
    #         self.amenity_ids.append(amenity_obj.id)
