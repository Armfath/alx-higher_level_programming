#!/usr/bin/python3
import unittest
from models.base import Base
import json
import inspect

'''
    Creating test cases for the base module
'''


class test_base(unittest.TestCase):
    '''
        Testing base
    '''
    def test_id_none(self):
        '''
            Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
            Sending a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
            Sending an id 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)