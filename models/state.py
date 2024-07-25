#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities_relationship = relationship('City', back_populates='state', cascade='all, delete')

    @property
    def cities(self):
        """Getter attribute cities that returns the list of City instances with state_id equals to the current State.id"""
        from models import storage
        return [city for city in storage.all(City).values() if city.state_id == self.id]
