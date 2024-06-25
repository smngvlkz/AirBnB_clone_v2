#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models import storage_type
from models.base_model import Base, BaseModel
from models.review import Review


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")

    if storage_type == "db":
        reviews = relationship(
            "Review", back_populates="place", cascade="all, delete-orphan"
        )
    else:

        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to the current Place.id"""
            from models import storage

            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
