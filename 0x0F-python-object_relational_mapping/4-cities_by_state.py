#!/usr/bin/python3
"""
This list all the cities in a state with
the city id and state name
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities JOIN \
                states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
