#!/usr/bin/python3
""" Model for the review inheriting from the base model """

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review model

    Arguments:
        place_id (str): Unique Place id.
        user_id (str): Unique user id.
        text (str): Review.
    """
    place_id = ""
    user_id = ""
    text = ""
