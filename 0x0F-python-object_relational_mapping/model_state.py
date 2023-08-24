#!/usr/bin/python3
"""
An sqlalchemy script based on State class and a base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
     """the state class links to the state table"""

    __tablename__ = 'state'

    id = Column(Integer, autoincreament=True primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
