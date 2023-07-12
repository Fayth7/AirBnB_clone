#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """ Common attributes of all sub classes """
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
            storage.new(self)

    def __str__(self) -> str:
        """ Returns: [class name] (ID) <class dictionary>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public updated_at with the current datetime """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the instance"""
        object_data = self.__dict__.copy()
        object_data['__class__'] = self.__class__.__name__
        object_data['created_at'] = self.created_at.isoformat()
        object_data['updated_at'] = self.updated_at.isoformat()

        return (object_data)
