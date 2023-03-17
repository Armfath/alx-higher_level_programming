#!/usr/bin/python3
"""
This module to use MySQLdb
"""
import sys
import MySQLdb


<<<<<<< HEAD
conn = MySQLdb.connect(user=args[0], passwd=args[1], db=args[2])
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC ")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
conn.close()
=======
if __name__ == "__main__":
    args = sys.argv[1:]
    conn = MySQLdb.connect(user=args[0], passwd=args[1], db=args[2])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
>>>>>>> 1271a878f37d452ec5f1aaf1d607efa2e7475886
