#!/usr/bin/python3
"""
Function module
"""


def is_same_class(obj, a_class):
    """
    check if the object is an instance of, or if
    the object is an
     instance of a class
     that
     inherited from, the specified class
    """

    return True if type(obj) == a_class else False
