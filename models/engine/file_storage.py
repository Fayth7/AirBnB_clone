#!/usr/bin/python3
""" File storage Class Model """

import json
import os
from models.base_model import BaseModel


class FileStorage():
    """ Serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "faith.json"
    __objects = {}
    # self.name = __class__.__name__ + str(id)

    def all(self):
        """ Returns the dictionary __objects """
        return (self.__objects)

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Serializes a class dict into a JSON file for storage"""

        with open(self.__file_path, 'w', encoding='utf-8') as viestar:
            storage_dic = {}
            for key, value in self.__objects.items():
                storage_dic[key] = value.to_dict()
            json.dump(storage_dic, viestar)

    def reload(self):
        """ Deserializes a JSON file back into a dictionary """
        # Incase file doesn't exist
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as faith:
                for object in json.load(faith).values():
                    self.new(eval(object["__class__"])(**object))
        else:
            return
