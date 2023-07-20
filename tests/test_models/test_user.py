#!/usr/bin/python3
""" Test suite for User class testing attributes, methods and ethinity """

import unittest

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ User test cases """

    def setUp(self):
        """ Test suite arrangements """
        self.user = User()

    def test_inheritance(self):
        """ IS user really a sub class of BaseModel """
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_email_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.user, "email"))

    def test_password_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.user, "password"))

    def test_first_name_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.user, "first_name"))

    def test_last_name_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_last_name_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.user, "age"))

    # Email
    def test_email_attr_type_string(self):
        """ Is the email sttributes of type STRING? """
        self.assertIs(type(self.user.email), str)

    def test_email_attr_type_not_int(self):
        """ Is the email sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.email), int)

    def test_email_attr_type_not_bool(self):
        """ Is the email sttributes of type BOOLEAN? """
        self.assertIsNot(type(self.user.email), bool)

    def test_email_attr_type_not_float(self):
        """ Is the email sttributes of type FLOAT? """
        self.assertIsNot(type(self.user.email), float)

    def test_non_email_attr_type(self):
        """ Is the email empty? """
        self.assertFalse(bool(getattr(self.user, "email")))

    # Password
    def test_password_attr_type_string(self):
        """ Is the password sttributes of type STRING? """
        self.assertIs(type(self.user.password), str)

    def test_password_attr_type_not_int(self):
        """ Is the password sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.password), int)

    def test_password_attr_type_not_float(self):
        """ Is the password sttributes of type FLOAT? """
        self.assertIsNot(type(self.user.password), float)

    def test_password_attr_type_not_bool(self):
        """ Is the password sttributes of type BOOLEAN? """
        self.assertIsNot(type(self.user.password), bool)

    def test_non_password_attr_type(self):
        """ Is the password sttributes of type INTEGER? """
        self.assertFalse(bool(getattr(self.user, "password")))

    # first name
    def test_first_name_attr_type_string(self):
        """ Is the first_name sttributes of type STRING? """
        self.assertIs(type(self.user.first_name), str)

    def test_first_name_attr_type_not_int(self):
        """ Is the first_name sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.first_name), int)

    def test_first_name_attr_type_not_bool(self):
        """ Is the first_name sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.first_name), bool)

    def test_first_name_attr_type_not_float(self):
        """ Is the first_name sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.first_name), float)

    def test_non_first_name_attr_type(self):
        """ Is the first_name sttributes of type INTEGER? """
        self.assertFalse(bool(getattr(self.user, "first_name")))

    # last name

    def test_last_name_attr_type_string(self):
        """ Is the last_name sttributes of type STRING? """
        self.assertIs(type(self.user.last_name), str)

    def test_last_name_attr_type_not_int(self):
        """ Is the last_name sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.last_name), int)

    def test_last_name_attr_type_not_float(self):
        """ Is the last_name sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.last_name), float)

    def test_last_name_attr_type_not_bool(self):
        """ Is the last_name sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.last_name), bool)

    def test_non_last_name_attr_empty(self):
        """ Is the last_name sttributes of type INTEGER? """
        self.assertFalse(bool(getattr(self.user, "last_name")))

    # age
    def test_age_attr_type_int(self):
        """ Is the age sttributes of type STRING? """
        self.assertIs(type(self.user.age), int)

    def test_age_attr_type_not_string(self):
        """ Is the age sttributes of type INTEGER? """
        self.assertIsNot(type(self.user.age), str)

    def test_age_attr_type_not_bool(self):
        """ Is the age sttributes of type BOOLEAN? """
        self.assertIsNot(type(self.user.age), bool)

    def test_age_attr_type_not_float(self):
        """ Is the age sttributes of type FLOAT? """
        self.assertIsNot(type(self.user.age), float)

    def test_non_age_attr_empty(self):
        """ Is the age empty? """
        self.assertFalse(bool(getattr(self.user, "age")))


if __name__ == "__main__":
    unittest.main()
