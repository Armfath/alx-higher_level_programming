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
    cur.execute('SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id=states.id \
            ORDER BY cities.id ASC')
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    conn.close()
