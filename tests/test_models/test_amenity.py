#!/usr/bin/python3
""" Test suite for Amenity class testing attributes, methods and ethinity """

import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Amenity test cases """

    def setUp(self):
        """ Test suite arrangements """
        self.amenity = Amenity()

    def test_inheritance(self):
        """ IS amenity really a sub class of BaseModel """
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attributes_type_string(self):
        """ Is the name sttributes of type STRING? """
        self.assertIs(type(self.amenity.name), str)

    def test_attributes_not_other_types(self):
        """ Is the name attribute not of type INTEGER? """
        self.assertIsNot(type(self.amenity.name), int)
        self.assertIsNot(type(self.amenity.name), float)
        self.assertIsNot(type(self.amenity.name), bool)

    def test_non_attributes_type(self):
        """ Is the name empty"""
        self.assertFalse(bool(getattr(self.amenity, "name")))


if __name__ == "__main__":
    unittest.main()
