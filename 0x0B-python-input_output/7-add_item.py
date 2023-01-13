#!/usr/bin/python3
"""
This module loads adds and saves in json
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    filename = "add_item.json"
    list = load_from_json_file(filename)
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            list.append(arg)
    save_to_json_file(list, filename)
except Exception as e:
    filename = "add_item.json"
    list = []
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            list.append(arg)
    save_to_json_file(list, filename)
    save_to_json_file(list, filename)
