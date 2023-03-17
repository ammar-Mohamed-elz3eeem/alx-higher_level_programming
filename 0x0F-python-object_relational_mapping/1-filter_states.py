#!/usr/bin/python3
"""
This is a module to select all states from db where name starts with Capital N
"""


import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY \
        'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    [print(row) for row in rows]

    cur.close()

    db.close()
