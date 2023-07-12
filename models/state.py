#!/usr/bin/python3
""" Model for the state inheriting from the base model """

from models.base_model import BaseModel


class State(BaseModel):
    """
    The State model

    Argument:
        name (str): State name.
    """
    name = ""
