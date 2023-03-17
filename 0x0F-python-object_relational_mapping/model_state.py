#!/usr/bin/python3
"""
This module is for creating state Class to be used
with sqlalchemy as ORM
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class:
        This class will be using to map to table states in database
    Args:
        Base: This is the Base class that states inherits from it
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
