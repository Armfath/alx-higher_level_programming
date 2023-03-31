#!/usr/bin/python3
"""
Python package requests usiing for HTTP requests
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io'
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
