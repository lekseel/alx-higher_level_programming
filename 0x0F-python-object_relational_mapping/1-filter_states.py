#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Take arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=dbname)

    # Create a cursor object
    cur = db.cursor()

    # Execute query to select all states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
