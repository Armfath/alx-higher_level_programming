#!/usr/bin/python3
"""
Function module
"""


def inherits_from(obj, a_class):
    """
    check if the object is an instance of, or if
    the object is an
     instance of a class
     that
     inherited from, the specified class
    """

    return any(isinstance(obj, subcls) for subcls in a_class.__subclasses__())
