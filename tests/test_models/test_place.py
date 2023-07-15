#!/usr/bin/python3
""" Test suite for Place class testing attributes, methods and ethinity """

import unittest

from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Place test cases """

    def setUp(self):
        """ Test suite arrangements """
        self.place = Place()
        self.attr_list = [
            "city_id",
            "user_id",
            "name",
            "description",
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            "latitude",
            "longitude",
            "amenity_ids"
        ]

    def test_inheritance(self):
        """ IS place really a sub class of BaseModel """
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_attributes_present(self):
        """ Does the class have all the attributes """
        for attribute in self.attr_list:
            self.assertTrue(hasattr(self.place, attribute))

    # Strings
    def test_attributes_of_type_string(self):
        """ Testing the data type of each variable"""
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.description), str)

    def test_attributes_of_type_not_int(self):
        """ Testing if these attributes are not integers"""
        self.assertIsNot(type(self.place.city_id), int)
        self.assertIsNot(type(self.place.user_id), int)
        self.assertIsNot(type(self.place.name), int)
        self.assertIsNot(type(self.place.description), int)

    def test_attributes_of_type_not_float(self):
        """ Testing if these attributes are not float"""
        self.assertIsNot(type(self.place.city_id), float)
        self.assertIsNot(type(self.place.user_id), float)
        self.assertIsNot(type(self.place.name), float)
        self.assertIsNot(type(self.place.description), float)

    def test_attributes_of_type_not_bool(self):
        """ Testing if these attributes are not bool"""
        self.assertIsNot(type(self.place.city_id), bool)
        self.assertIsNot(type(self.place.user_id), bool)
        self.assertIsNot(type(self.place.name), bool)
        self.assertIsNot(type(self.place.description), bool)

    # Integers

    def test_attributes_of_type_int(self):
        """ Integers """
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), int)

    def test_int_attributes_of_type_not_str(self):
        """ Integers """
        self.assertIsNot(type(self.place.number_rooms), str)
        self.assertIsNot(type(self.place.number_bathrooms), str)
        self.assertIsNot(type(self.place.max_guest), str)
        self.assertIsNot(type(self.place.price_by_night), str)

    def test_int_attributes_of_type_not_bool(self):
        """ Integers """
        self.assertIsNot(type(self.place.number_rooms), bool)
        self.assertIsNot(type(self.place.number_bathrooms), bool)
        self.assertIsNot(type(self.place.max_guest), bool)
        self.assertIsNot(type(self.place.price_by_night), bool)

    def test_int_attributes_of_type_not_float(self):
        """ Integers """
        self.assertIsNot(type(self.place.number_rooms), float)
        self.assertIsNot(type(self.place.number_bathrooms), float)
        self.assertIsNot(type(self.place.max_guest), float)
        self.assertIsNot(type(self.place.price_by_night), float)

    # Floats
    def test_attributes_of_type_float(self):
        """ Floats """
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)

    def test_float_attributes_of_type_not_int(self):
        """ ints """
        self.assertIsNot(type(self.place.latitude), int)
        self.assertIsNot(type(self.place.longitude), int)

    def test_float_attributes_of_type_not_str(self):
        """ strs """
        self.assertIsNot(type(self.place.latitude), str)
        self.assertIsNot(type(self.place.longitude), str)

    def test_float_attributes_of_type_not_bool(self):
        """ bools """
        self.assertIsNot(type(self.place.latitude), bool)
        self.assertIsNot(type(self.place.longitude), bool)

    def test_attributes_of_type_list(self):
        """ list """
        self.assertIs(type(self.place.amenity_ids), list)

    def test_attributes_defualt_value(self):
        """ Default values"""
        for attribute in self.attr_list:
            self.assertFalse(bool(getattr(self.place, attribute)))


if __name__ == "__main__":
    unittest.main()
