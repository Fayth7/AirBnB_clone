#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Common attributes of all subclasses"""
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.age = None  # Add the age attribute
            self.password = None  # Add the password attribute
            self.email = None  # Add the email attribute
            storage.new(self)

    def __str__(self) -> str:
        """Returns: [class name] (ID) <class dictionary>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public updated_at with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
            object_dict[key] = value
        return object_dict
