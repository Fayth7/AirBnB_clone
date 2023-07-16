#!/usr/bin/python3
"""Test suite for HBNBCommand class testing attributes, methods, and functionality"""

import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand


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


if __name__ == "__main__":
    unittest.main()
