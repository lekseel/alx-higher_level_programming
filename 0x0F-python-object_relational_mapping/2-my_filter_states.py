#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa where
name matches the argument passed to the script
"""
import MySQLdb
import sys


def filter_states():
    """
    Function that filters and displays the states that match the user input
    """
    # Connect to MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")

    # Create cursor to execute queries
    cur = conn.cursor()

    # Execute SQL query with user input and sort results by states.id
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(sys.argv[4]))

    # Fetch all rows and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_states()
