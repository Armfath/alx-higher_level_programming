#!/usr/bin/python3
"""
This module contain function relate to JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Rturns an object (Python data structure) represented by a JSON string
    """
    with open(filename, mode='w') as file:
        json_data = json.dumps(my_obj)
        file.write(json_data)
