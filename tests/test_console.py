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


if __name__ == "__main__":
    unittest.main()
