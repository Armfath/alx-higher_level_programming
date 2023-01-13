#!/usr/bin/python3
"""
This module contain function relate to JSON
"""
import json


def load_from_json_file(filename):
    """
    Rturns an object (Python data structure) represented by a JSON string
    """
    with open(filename, mode='r') as file:
        object = json.load(file)

        return object
