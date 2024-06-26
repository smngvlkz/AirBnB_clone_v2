#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)
    
    if models.storage_type == 'db':
        place_amenities = relationship("Place", secondary="place_amenity", 
                                       back_populates="amenities")
    else:
        place_amenities = []

        @property
        def places(self):
            """Returns the list of Place instances with amenity_ids containing the current Amenity.id"""
            from models.place import Place
            return [place for place in models.storage.all(Place).values() 
                    if self.id in place.amenity_ids]
