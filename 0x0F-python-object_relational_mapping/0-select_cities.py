#!/usr/bin/python3
"""
This module to use MySQLdb
"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv[1:]
    conn = MySQLdb.connect(user=args[0], passwd=args[1], db=args[2])
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    conn.close()
