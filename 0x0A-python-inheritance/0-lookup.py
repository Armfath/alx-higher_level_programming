#!/usr/bin/python3
"""
Returns the dic of an object
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    list = []
    for var in obj.__dict__:
        list.append(var)

    return list
