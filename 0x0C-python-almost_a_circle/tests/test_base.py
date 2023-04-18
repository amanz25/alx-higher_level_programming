#!/usr/bin/python3
"""ünit test"""
import unittest
from models import Square
import inspect
from io import StringIO
import pep8
from models.base import Base
import json
from models import Rectangle
import os


class TestBase(unittest.TestCase):
    """testcase/collection of tests"""
    def docstrings_test(self):
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIs(hasattr(Base, "create"), True)

    def from_json_string_test(self):
        """test from_json_string method"""
        self.assertEqual(Base.to_json_string([]), "[]")
        rec = Rectangle(59, 7, 15, 45, 9)
        self.assertEqual(rec.to_dictionary(), {'x': 15, 'width': 59,
                                               'id': 9, 'height': 7,
                                               'y': 45})

    def rectangle_test(self):
        """test a rectangle"""
        rec = Rectangle(26, 59, 85)
        oth = Rectangle.create(**(rec.to_dictionary()))
        self.assertNotEqual(rec, oth)

    def square_test(self):
        """test a square"""
        rec = Square(26, 59, 85, 56)
        oth = Rectangle.create(**(rec.to_dictionary()))
        self.assertNotEqual(rec, oth)
