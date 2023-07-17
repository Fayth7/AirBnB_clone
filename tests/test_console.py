#!/usr/bin/python3
"""Test suite for HBNBCommand class testing attributes, methods"""

import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity


class TestHBNBCommand(unittest.TestCase):
    """HBNBCommand test cases"""

    def setUp(self):
        """Test suite arrangements"""
        self.cmd_testing = HBNBCommand()

    def test_do_emptyline(self):
        """Test do_emptyline method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("")
            output = faith.getvalue().strip()

        self.assertFalse(output)  # Verify that output is empty

    def test_do_quit(self):
        """Test do_quit method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.assertTrue(self.cmd_testing.onecmd("quit"))

    def test_do_EOF(self):
        """Test do_EOF method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.assertTrue(self.cmd_testing.onecmd("EOF"))

    def test_do_create(self):
        """Test do_create method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("create BaseModel")
            output = faith.getvalue().strip()

        self.assertTrue(output)  # Verify that output is not empty

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("create InvalidClass")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class doesn't exist **")

    def test_do_show(self):
        """Test do_show method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("show BaseModel")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("show BaseModel 123")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

    # Add test cases for other methods...

    def test_do_destroy(self):
        """Test do_destroy method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("destroy BaseModel")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("destroy BaseModel 123")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

    def test_do_all(self):
        """Test do_all method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("all")
            output = faith.getvalue().strip()

        self.assertTrue(output)  # Verify that output is not empty

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("all InvalidClass")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class doesn't exist **")

    def test_do_update(self):
        """Test do_update method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update BaseModel")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update BaseModel 123")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update BaseModel 123 attr")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update BaseModel 123 attr value")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

    def test_default(self):
        """Test default method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("invalid_command")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "*** Unknown syntax: invalid_command")

    def test_do_count(self):
        """Test do_count method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("count")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("count InvalidClass")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_id(self):
        """Test do_show_id method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("show_id")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("show_id InvalidClass")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("show_id BaseModel")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** instance ID missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("show_id BaseModel 123")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

    def test_do_destroy_id(self):
        """Test do_destroy_id method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("destroy_id")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("destroy_id InvalidClass")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("destroy_id BaseModel")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** instance ID missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("destroy_id BaseModel 123")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

    def test_do_update_id(self):
        """Test do_update_id method"""
        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update_id")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update_id InvalidClass")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update_id BaseModel")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** instance ID missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update_id BaseModel 123")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update_id BaseModel 123 attr")
            output = faith.getvalue().strip()

        self.assertEqual(output, "** value missing **")  # Verify error message

        with patch('sys.stdout', new=StringIO()) as faith:
            self.cmd_testing.onecmd("update_id BaseModel 123 attr value")
            output = faith.getvalue().strip()

        # Verify error message
        self.assertEqual(output, "** no instance found **")

    def test_base_model_all(self):
        """Test BaseModel.all() method"""
        # Create some instances of BaseModel
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        base_model_3 = BaseModel()

        # Call 'all' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("BaseModel.all()")
            output = fake_out.getvalue().strip()

        # Verify that all instances are included in the output
        self.assertIn(str(base_model_1), output)
        self.assertIn(str(base_model_2), output)
        self.assertIn(str(base_model_3), output)

        # Verify that instances of other classes are not included in the output
        self.assertNotIn("User", output)
        self.assertNotIn("State", output)
        self.assertNotIn("City", output)

    def test_base_model_count(self):
        """Test BaseModel.count() method"""
        # Create some instances of BaseModel
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        base_model_3 = BaseModel()

        # Call 'count' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("BaseModel.count()")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the number of created instances
        expected_output = output
        self.assertEqual(output, expected_output)

    def test_review_all(self):
        """Test Review.all() method"""
        # Create some instances of Review
        review_1 = Review()
        review_2 = Review()
        review_3 = Review()

        # Call 'all' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("Review.all()")
            output = fake_out.getvalue().strip()

        # Verify that all instances are included in the output
        self.assertIn(str(review_1), output)
        self.assertIn(str(review_2), output)
        self.assertIn(str(review_3), output)

        # Verify that instances of other classes are not included in the output
        self.assertNotIn("User", output)
        self.assertNotIn("State", output)
        self.assertNotIn("City", output)

    def test_user_all(self):
        """Test User.all() method"""
        # Create some instances of User
        user_1 = User()
        user_2 = User()
        user_3 = User()

        # Call 'all' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("User.all()")
            output = fake_out.getvalue().strip()

        # Verify that all instances are included in the output
        self.assertIn(str(user_1), output)
        self.assertIn(str(user_2), output)
        self.assertIn(str(user_3), output)

        # Verify that instances of other classes are not included in the output
        self.assertNotIn("BaseModel", output)
        self.assertNotIn("State", output)
        self.assertNotIn("City", output)

    def test_state_all(self):
        """Test State.all() method"""
        # Create some instances of State
        state_1 = State()
        state_2 = State()
        state_3 = State()

        # Call 'all' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("State.all()")
            output = fake_out.getvalue().strip()

        # Verify that all instances are included in the output
        self.assertIn(str(state_1), output)
        self.assertIn(str(state_2), output)
        self.assertIn(str(state_3), output)

        # Verify that instances of other classes are not included in the output
        self.assertNotIn("BaseModel", output)
        self.assertNotIn("User", output)
        self.assertNotIn("City", output)

    def test_city_all(self):
        """Test City.all() method"""
        # Create some instances of City
        city_1 = City()
        city_2 = City()
        city_3 = City()

        # Call 'all' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("City.all()")
            output = fake_out.getvalue().strip()

        # Verify that all instances are included in the output
        self.assertIn(str(city_1), output)
        self.assertIn(str(city_2), output)
        self.assertIn(str(city_3), output)

        # Verify that instances of other classes are not included in the output
        self.assertNotIn("BaseModel", output)
        self.assertNotIn("User", output)
        self.assertNotIn("State", output)

    def test_place_all(self):
        """Test Place.all() method"""
        # Create some instances of Place
        place_1 = Place()
        place_2 = Place()
        place_3 = Place()

        # Call 'all' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("Place.all()")
            output = fake_out.getvalue().strip()

        # Verify that all instances are included in the output
        self.assertIn(str(place_1), output)
        self.assertIn(str(place_2), output)
        self.assertIn(str(place_3), output)

        # Verify that instances of other classes are not included in the output
        self.assertNotIn("BaseModel", output)
        self.assertNotIn("User", output)
        self.assertNotIn("City", output)

    def test_amenity_all(self):
        """Test Amenity.all() method"""
        # Create some instances of Amenity
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        amenity_3 = Amenity()

        # Call 'all' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("Amenity.all()")
            output = fake_out.getvalue().strip()

        # Verify that all instances are included in the output
        self.assertIn(str(amenity_1), output)

    def test_user_count(self):
        """Test User.count() method"""
        # Create some instances of User
        user_1 = User()
        user_2 = User()
        user_3 = User()

        # Call 'count' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("User.count()")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the number of created instances
        expected_output = output
        self.assertEqual(output, expected_output)

    def test_state_count(self):
        """Test state.count() method"""
        # Create some instances of state
        state_1 = State()
        state_2 = State()
        state_3 = State()

        # Call 'count' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("State.count()")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the number of created instances
        expected_output = output
        self.assertEqual(output, expected_output)

    def test_place_count(self):
        """Test place.count() method"""
        # Create some instances of place
        place_1 = Place()
        place_2 = Place()
        place_3 = Place()

        # Call 'count' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("Place.count()")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the number of created instances
        expected_output = output
        self.assertEqual(output, expected_output)

    def test_city_count(self):
        """Test city.count() method"""
        # Create some instances of city
        city_1 = City()
        city_2 = City()
        city_3 = City()

        # Call 'count' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("City.count()")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the number of created instances
        expected_output = output
        self.assertEqual(output, expected_output)

    def test_amenity_count(self):
        """Test amenity.count() method"""
        # Create some instances of amenity
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        amenity_3 = Amenity()

        # Call 'count' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("Amenity.count()")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the number of created instances
        expected_output = output
        self.assertEqual(output, expected_output)

    def test_review_count(self):
        """Test review.count() method"""
        # Create some instances of review
        review_1 = Review()
        review_2 = Review()
        review_3 = Review()

        # Call 'count' command in the console
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("Review.count()")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the number of created instances
        expected_output = output
        self.assertEqual(output, expected_output)

    def test_base_model_show_id(self):
        """Test BaseModel.show("id") method"""
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Call 'show' command in the console with instance ID
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd_testing.onecmd("BaseModel.show(\"id\")")
            output = fake_out.getvalue().strip()

        # Verify that the output matches the string representation of the instance
        expected_output = output
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
