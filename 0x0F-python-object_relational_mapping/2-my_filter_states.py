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
    slt = "SELECT * FROM states "
    cur.execute("%s WHERE name = BINARY '{}' ORDER BY id ASC".format(args[3]) % (slt))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
