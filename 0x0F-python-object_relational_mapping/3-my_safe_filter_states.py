#!/usr/bin/python3
"""
This takes an argument and displays the vlaues in the
state that match with the argument in the database
These also prevents sql injections
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
