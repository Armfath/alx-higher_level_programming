#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
import math
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Enssential tests cases
    """
    def test_correct_value(self):
        """
        Tests correct output
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_errors(self):
        """
        Tests errors
        """
        with self.assertRaises(TypeError):
            max_integer(2)
        with self.assertRaises(TypeError):
            max_integer(["t", 3, 4, 2])

    def test_bording_value(self):
        """
        Tests baords cases
        """
        self.assertTrue(math.isnan(max_integer([float('nan'), 2])))
        self.assertTrue(math.isinf(max_integer([float('inf'), 2])))
