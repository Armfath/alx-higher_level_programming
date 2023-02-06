#!/usr/bin/python3
"""
Tests for base class
"""


import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """
    Base tests
    """

    def test_basics(self):
        """
        Tests basics values
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
if __name__ == '__main__':
    unittest.main()
