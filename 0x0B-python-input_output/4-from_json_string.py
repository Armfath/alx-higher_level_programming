#!/usr/bin/python3
"""
This module contain function relate to JSON
"""
import json


def from_json_string(my_str):
    """
    Rturns an object (Python data structure) represented by a JSON string
    """

    return json.loads(my_str)
