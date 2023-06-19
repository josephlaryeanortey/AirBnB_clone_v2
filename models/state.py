#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlachmy import Column, String
from sqlachmy.orm import relationship
from models import storage_type


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='delete, all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """relationship between city and state"""
            from models import storage
            new_city = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    new_city.append(city)
            return new_city
