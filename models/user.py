#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.base_model import Base
from models.base_model import BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place",
                          back_populates="user",
                          cascade="all, delete-orphan")
    reviews = relationship("Review",
                           back_populates="user",
                           cascade="all, delete-orphan")
