#!/usr/bin/python3
"""
this module is for creating city class to be mapped
with city table using sqlalchmey ORM
"""


from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    City class:
        This class will be using to map to table cities in database
    Args:
        Base: This is the Base class that City inherits from it
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
