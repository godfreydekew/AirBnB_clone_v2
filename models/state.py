#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def cities(self):
        """Getter method for cities"""
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
