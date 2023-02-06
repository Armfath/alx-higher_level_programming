#!/usr/bin/python3
"""
Tests for base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Base tests
    """

    def test_basics(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)
