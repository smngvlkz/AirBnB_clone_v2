#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    
    state = relationship("State", back_populates="cities_relationship")
    places = relationship("Place", back_populates="city", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initialization of the City instance"""
        super().__init__(*args, **kwargs)
