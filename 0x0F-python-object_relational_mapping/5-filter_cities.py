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
    cur.execute('SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id=states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC', (args[3],))
    cities = cur.fetchall()
    i = 0
    for city in cities:
        print(city[0], end='')
        i += 1
        if i != len(cities):
            print(', ', end='')
    print()
    cur.close()
    conn.close()
