#!/usr/bin/python3
"""
This module contain function relate to JSON
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename, mode='r') as file:
        object = json.load(file)

        return object
