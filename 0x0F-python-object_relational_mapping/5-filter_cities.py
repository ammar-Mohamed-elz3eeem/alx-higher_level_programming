#!/usr/bin/python3
"""
This is a module to select all cities from db in ascending order
that matches search keyword argument given in program arguments
but avoiding SQL injection
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    cur = db.cursor()

    sql = """SELECT city.name FROM cities city
    INNER JOIN states state ON state.id = city.state_id
    WHERE state.name LIKE BINARY %s
    ORDER BY city.id ASC"""

    cur.execute(sql, (sys.argv[4],))
    rows = cur.fetchall()
    for i in range(cur.rowcount):
        print(rows[i][0], end="")
        if i < cur.rowcount - 1:
            print(", ", end="")
    print()
    cur.close()
    db.close()
