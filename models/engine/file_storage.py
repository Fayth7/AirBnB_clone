#!/usr/bin/python3
""" File storage Class Model"""


import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes a class dict into a JSON file for storage"""
        storage_dict = {}
        for key, value in self.__objects.items():
            storage_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(storage_dict, file)

    def reload(self):
        """Deserializes a JSON file back into a dictionary"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objects_dict = json.load(file)
                for obj_dict in objects_dict.values():
                    class_name = obj_dict['__class__']
                    obj_id = obj_dict['id']
                    module = __import__('models.' + class_name,
                                        globals(), locals(), [class_name], 0)
                    class_ = getattr(module, class_name)
                    obj_instance = class_(**obj_dict)
                    self.__objects[class_name + '.' + obj_id] = obj_instance
        except FileNotFoundError:
            pass
