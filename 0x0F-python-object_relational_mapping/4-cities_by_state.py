#!/usr/bin/python3
"""
This is a module to select all states from db in ascending order
that matched search keyword argument given in program arguments
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

    sql = """SELECT city.id, city.name, state.name FROM cities city
    INNER JOIN states state ON state.id = city.state_id ORDER BY city.id ASC"""

    cur.execute(sql)
    rows = cur.fetchall()
    [print(row) for row in rows]

    cur.close()
    db.close()
