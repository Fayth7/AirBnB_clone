#!/usr/bin/python3
""" Model for the city inheriting from the base model """

from models.base_model import BaseModel


class City(BaseModel):
    """
    The City model

    Arguments:
        state_id (str): Unique State id.
        name (str): State name.
    """
    state_id = ""
    name = ""
