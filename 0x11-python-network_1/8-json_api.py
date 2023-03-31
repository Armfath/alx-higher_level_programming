#!/usr/bin/python3
"""
Python package requests usiing for HTTP requests
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    value = sys.argv[1] if len(sys.argv) >= 2 else ""
    param = {'q': value}
    r = requests.post(url, data=param)
    try:
        if not r.json():
            print('No result')
        else:
            json_r = r.json()
            print(f"[{json_r['id']}] {json_r['name']}")
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
