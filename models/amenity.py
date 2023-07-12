#!/usr/bin/python3
""" Model for the amenity inheriting from the base model """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The Amenity model

    Argument:
        name (str): Amenity name.
    """
    name = ""
