#!/usr/bin/python3
""" Test suite for City class testing attributes, methods and ethinity """

import unittest

from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ City test cases """

    def setUp(self):
        """ Test suite arrangements """
        self.object_one = BaseModel()
        self.object_two = BaseModel()
        self.object_three = BaseModel()
        self.object_four = BaseModel()

    def test_BaseModel_has_id(self):
        """ Signed ID on initialization? """
        self.assertTrue(hasattr(self.object_one, "id"))

    def test_well_str_representation(self):
        """String representation appropriate? """
        self.assertEqual(str(
            self.object_one),
            f"[BaseModel] ({self.object_one.id}) {self.object_one.__dict__}")

    def test_ids_unique(self):
        """ Unique IDs?  """
        self.assertNotEqual(self.object_one.id, self.object_two.id)
        self.assertNotEqual(self.object_three.id, self.object_four.id)

    def test_type_of_id_is_str(self):
        """ ID String? """
        self.assertTrue(type(self.object_four.id) is str)
        self.assertTrue(type(self.object_three.id) is str)

    def test_type_of_id_is_not_int(self):
        """ ID not Integer? """
        self.assertFalse(type(self.object_four.id) is int)
        self.assertFalse(type(self.object_three.id) is int)

    def test_created_at_of_datetime(self):
        """ 'created_at' of datetime """
        self.assertTrue(type(self.object_one.created_at) is datetime)

    def test_updated_at_of_datetime(self):
        """ 'updated_at' of datetime? """
        self.assertTrue(type(self.object_one.updated_at) is datetime)

    def test_created_at_not_string(self):
        """ 'created_at' of datetime """
        self.assertFalse(type(self.object_one.created_at) is str)

    def test_updated_not_string(self):
        """ 'updated_at' of datetime? """
        self.assertFalse(type(self.object_one.updated_at) is str)


if __name__ == "__main__":
    unittest.main()
