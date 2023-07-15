#!/usr/bin/python3
""" Test suite for City class testing attributes, methods and ethinity """

import unittest

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ City test cases """

    def setUp(cls):
        """ Test suite arrangements """
        cls.city = City()

    def test_city_inheritance(cls):
        """ IS city really a sub class of BaseModel """
        cls.assertTrue(issubclass(type(cls.city), BaseModel))

    # Testing name attribute
    def test_name_attributes_present(cls):
        """ Does the class have all the attributes """
        cls.assertTrue(hasattr(cls.city, "name"))

    def test_name_attr_type_string(cls):
        """ Is the name sttributes of type STRING? """
        cls.assertIs(type(cls.city.name), str)

    def test_name_attr_type_not_int(cls):
        """ Is the name sttribute not of type INTEGER? """
        cls.assertIsNot(type(cls.city.name), int)

    def test_name_attr_type_not_float(cls):
        """ Is the name sttribute not of type FLOAT? """
        cls.assertIsNot(type(cls.city.name), float)

    def test_name_attr_type_not_bool(cls):
        """ Is the name sttribute not of type BOOLEAN? """
        cls.assertIsNot(type(cls.city.name), bool)

    def test_non_name_attr_type(cls):
        """ Is the name empty """
        cls.assertFalse(bool(getattr(cls.city, "name")))

# Testing state_id attribute
    def test_state_id_attributes_present(cls):
        """ Does the class have all the attributes """
        cls.assertTrue(hasattr(cls.city, "state_id"))

    def test_state_id_attr_type_string(cls):
        """ Is the state_id sttributes of type STRING? """
        cls.assertIs(type(cls.city.state_id), str)

    def test_state_id_attr_type_not_int(cls):
        """ Is the state_id sttribute not of type INTEGER? """
        cls.assertIsNot(type(cls.city.state_id), int)

    def test_state_id_attr_type_not_float(cls):
        """ Is the state_id sttribute not of type FLOAT? """
        cls.assertIsNot(type(cls.city.state_id), float)

    def test_state_id_attr_type_not_bool(cls):
        """ Is the state_id sttribute not of type BOOLEAN? """
        cls.assertIsNot(type(cls.city.state_id), bool)

    def test_non_state_id_attr_type(cls):
        """ Is the state_id empty """
        cls.assertFalse(bool(getattr(cls.city, "state_id")))


if __name__ == "__main__":
    unittest.main()
