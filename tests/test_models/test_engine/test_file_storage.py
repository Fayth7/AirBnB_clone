#!/usr/bin/python3
""" Test suite for FileStorage class testing attributes, methods """

import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ FileStorage test cases """

    def setUp(self):
        """ Test suite arrangements """
        self.storage = FileStorage()
        self.city = City()
        self.city.name = "Kampala"
        self.user = User()
        self.user.name = "Silvester Schmitzer"
        self.storage.new(self.city)
        self.storage.new(self.user)

    def tearDown(self):
        """ Clean up after each test """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """ Test the all() method """
        all_objects = self.storage.all()
        # self.assertEqual(len(all_objects), 2)
        self.assertIn("City." + self.city.id, all_objects)
        self.assertIn("User." + self.user.id, all_objects)
        self.assertIs(all_objects["City." + self.city.id], self.city)
        self.assertIs(all_objects["User." + self.user.id], self.user)

    def test_new(self):
        """ Test the new() method """
        new_city = City()
        new_city.name = "Paris"
        self.storage.new(new_city)
        all_objects = self.storage.all()
        self.assertIn("City." + new_city.id, all_objects)
        self.assertIs(all_objects["City." + new_city.id], new_city)

    def test_save(self):
        """ Test the save() method """
        self.storage.save()
        self.assertTrue(os.path.exists("faith.json"))
        with open("faith.json", "r") as file:
            data = json.load(file)
            self.assertIn("City." + self.city.id, data)
            self.assertIn("User." + self.user.id, data)

    def test_reload(self):
        """ Test the reload() method """
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        # self.assertEqual(len(all_objects), 2)
        self.assertIn("City." + self.city.id, all_objects)
        self.assertIn("User." + self.user.id, all_objects)
        self.assertIsNot(all_objects["City." + self.city.id], self.city)
        self.assertIsNot(all_objects["User." + self.user.id], self.user)
        self.assertIsInstance(all_objects["City." + self.city.id], City)
        self.assertIsInstance(all_objects["User." + self.user.id], User)


if __name__ == "__main__":
    unittest.main()
