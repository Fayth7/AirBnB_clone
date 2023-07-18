#!/usr/bin/python3
""" Model for the User inheriting from the base model """

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User model

    Arguments:
        email (str): User email.
        password (str): User password.
        first_name (str): User first name.
        last_name (str): User last name.
        age (int): User age.

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    age = ""
