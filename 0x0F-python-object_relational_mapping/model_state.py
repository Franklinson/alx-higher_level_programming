#!/usr/bin/python3
"""
An sqlalchemy script based on State class and a base
"""

from sqllchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'State'

    id = Column(integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
