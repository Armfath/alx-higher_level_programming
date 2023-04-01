#!/usr/bin/python3
"""
Python package requests usiing for HTTP requests
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        commits = r.json()
        r_last_10 = commits[-10:]
        for i in r_last_10:
            print(f"{i['sha']}: {i['commit']['author']['name']}")
