#!/usr/bin/python3
""" Model for the place inheriting from the base model """

from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place model

    Arguments:
        city_id (str): Unique City id.
        user_id (str): Unique user id.
        name (str): Place name.
        description (str): Place Description.
        number_rooms (int): Number of the rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Maximum number of guests.
        price_by_night (int): Price by night.
        latitude (float): Place latitude.
        longitude (float): Place longitude.
        amenity_ids (list): A list of Amenity ids.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
