#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models


place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")

    if models.storage_type == 'db':
        amenities = relationship("Amenity", secondary=place_amenity,
                                 back_populates="place_amenities", viewonly=False)
    else:
        @property
        def amenities(self):
            """Getter attribute for FileStorage returns the list of Amenity instances"""
            from models.amenity import Amenity
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute for FileStorage that handles append for adding an Amenity.id"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.idi)
