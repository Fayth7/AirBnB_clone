#!/usr/bin/python3
""" Model for the User inheriting from the base model """

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User model

    Arguments:
        email (str): Unique City id.
        password (str): User password.
        first_name (str): User first name.
        last_name (str): User last nae.

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

  @classmethod
    def all(cls):
        """Return a list of all User instances"""
        from models import storage
        return [obj for obj in storage.all().values() if isinstance(obj, cls)]
