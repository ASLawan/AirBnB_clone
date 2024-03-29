#!/usr/bin/python3
"""
    Module to implement class Place, that inherits
    from base class BaseModel

"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place that instantiates place instances"""
    city_id = ""   # city.id
    user_id = ""   # user.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []   # empty list to be filled
