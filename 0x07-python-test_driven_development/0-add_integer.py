#!/usr/bin/python3
"""
Containing mathematicams opparations

raiose exception error for type
"""


def add_integer(a, b=98):
    """
    adds two integers
    """
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
