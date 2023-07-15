#!/usr/bin/python3
""" Test suite for State class testing attributes, methods and ethinity """

import unittest

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ State test cases """

    def setUp(self):
        """ Test suite arrangements """
        self.state = State()

    def test_state_inheritance(self):
        """ IS state really a sub class of BaseModel """
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.state, "name"))

    def test_attributes_type_string(self):
        """ Is the name sttributes of type STRING? """
        self.assertIs(type(self.state.name), str)

    def test_attributes_type_not_int(self):
        """ Is the name attribute not of type INTEGER? """
        self.assertIsNot(type(self.state.name), int)

    def test_attributes_type_not_float(self):
        """ Is the name attribute not of type FLOAT? """
        self.assertIsNot(type(self.state.name), float)

    def test_attributes_type_not_bool(self):
        """ Is the name attribute not of type BOOLEAN? """
        self.assertIsNot(type(self.state.name), bool)

    def test_attribute_empty(self):
        """ Is the name empty? """
        self.assertFalse(bool(getattr(self.state, "name")))


if __name__ == "__main__":
    unittest.main()
