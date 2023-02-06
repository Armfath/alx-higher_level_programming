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

    def test_id_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            Sending a valid id ok ?
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
            Sending an id 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            Sending a negative id
        '''
        b = Base(-20)
        self.assertEqual(-20, b.id)
