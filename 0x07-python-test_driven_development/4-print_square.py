#!/usr/bin/python3
"""
Module for drawing square

Test actions
"""


def print_square(size):
    """"
    Draw a square and handle errors
    """
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end='')
        print()
