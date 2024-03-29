#!/usr/bin/python3
"""
This is a module to select all states from db in ascending order
that matched search keyword argument given in program arguments
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         port=3306,
                         db=sys.argv[3])

    cur = db.cursor()

    sql = """SELECT * FROM states WHERE
    name LIKE BINARY '{}' ORDER BY id""".format(sys.argv[4])

    cur.execute(sql)
    data = cur.fetchall()
    [print(row) for row in data]
    cur.close()
    db.close()
