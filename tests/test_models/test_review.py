#!/usr/bin/python3
""" Test suite for Review class testing attributes, methods and ethinity """

import unittest

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Review test cases """

    def setUp(self):
        """ Test suite arrangements """
        self.review = Review()

    def test_review_inheritance(self):
        """ IS review really a sub class of BaseModel """
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_place_id_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.review, "place_id"))

    def test_user_id_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.review, "user_id"))

    def test_text_attributes_present(self):
        """ Does the class have all the attributes """
        self.assertTrue(hasattr(self.review, "text"))

    def test_place_id_attr_type_string(self):
        """ Is the place_id sttributes of type STRING? """
        self.assertIs(type(self.review.place_id), str)

    def test_place_id_attr_type_not_int(self):
        """ Is the place_id sttributes of type INTEGER? """
        self.assertIsNot(type(self.review.place_id), int)

    def test_non_place_id_attr_empty(self):
        """ Is the place_id empty """
        self.assertFalse(bool(getattr(self.review, "place_id")))

    def test_user_id_attr_type_string(self):
        """ Is the user_id sttributes of type STRING? """
        self.assertIs(type(self.review.user_id), str)

    def test_user_id_attr_type_not_int(self):
        """ Is the user_id sttributes of type INTEGER? """
        self.assertIsNot(type(self.review.user_id), int)

    def test_non_user_id_attr_empty(self):
        """ Is the user_id empty """
        self.assertFalse(bool(getattr(self.review, "user_id")))

    def test_text_attr_type_string(self):
        """ Is the text sttributes of type STRING? """
        self.assertIs(type(self.review.text), str)

    def test_text_attr_type_not_int(self):
        """ Is the text sttributes of type INTEGER? """
        self.assertIsNot(type(self.review.text), int)

    def test_non_text_attr_empty(self):
        """ Is the text empty """
        self.assertFalse(bool(getattr(self.review, "text")))


if __name__ == "__main__":
    unittest.main()
