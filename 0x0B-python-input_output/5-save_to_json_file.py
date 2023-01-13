#!/usr/bin/python3
"""
This module contain function relate to JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode='w') as file:
        json_data = json.dumps(my_obj)
        file.write(json_data)
