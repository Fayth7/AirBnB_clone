#!/usr/bin/python3
from datetime import datetime, timezone, timedelta
import uuid
import json
import os


class BaseModel():
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self):
        """ Common attributes of all sub classes """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    @classmethod
    def do_save(cls):
        """ Saves a new user to the file storage """
        obj = BaseModel()
        object_data = {
            "id": obj.id,
            "created_at": obj.created_at,
            "updated_at": obj.updated_at
        }

        # If the file already exists, we append to avoid overwriting objects.
        file_path = 'engine/json_object_file.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as faith:
                objects = json.load(faith)
        else:
            objects = []
        objects.append(object_data)

        BaseModel.do_to_json(objects, file_path)

        return f"User: {obj.id} has been created at {obj.created_at} and updated at {obj.updated_at}"

    @staticmethod
    def do_to_json(object_data, file_path):
        """ Serializes a class into a JSON file for storage """
        with open(file_path, "w") as viestar:
            json.dump(object_data, viestar)


print(BaseModel.do_save())
