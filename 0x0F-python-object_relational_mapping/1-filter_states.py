#!/usr/bin/python3
"""
This module to use MySQLdb
"""
import sys
import MySQLdb

args = sys.argv[1:]

conn = MySQLdb.connect(user=args[0], passwd=args[1], db=args[2], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'A%' ORDER BY id ASC ")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
conn.close()
