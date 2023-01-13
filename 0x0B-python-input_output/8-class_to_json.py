#!/usr/bin/python3
"""
This module loads adds and saves in json
"""


def class_to_json(obj):
    """
    returns the dictionary description for JSON serialization of an object
    """

    des = {}
    des = obj.__dict__
    return des
