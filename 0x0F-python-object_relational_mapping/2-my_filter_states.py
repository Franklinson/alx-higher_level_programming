#!/usr/bin/python3
"""
This takes an argument in the command line and displays the values in the state that match the argument from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    #usr = argv[1]
    #usr_pass = argv[2]
    #db_name = argv[3]

    conn = MySQLdb.connect(
            host-"localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM staes WHERE (name) LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(argv[4]))

    rows = cur,fetchall()
    for row in rows:
        print(row)
