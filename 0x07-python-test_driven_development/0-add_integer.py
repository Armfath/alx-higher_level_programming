#!/usr/bin/python3
"""
Containing mathematicams opparations

raise exception error for type
"""


def add_integer(a, b=98):
    """
    adds two integers
    """
    if not(isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    else:
        a = int(a)
            
    if not(isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    else:
        b = int(b)
    return a + b
