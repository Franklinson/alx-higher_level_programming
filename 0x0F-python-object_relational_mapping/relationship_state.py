#!/usr/bin/python3
"""
This script defines a State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
