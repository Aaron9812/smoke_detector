# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor

cur = conn.cursor()

#retrieving information 
some_name = "Aaron" 
cur.execute("SELECT * FROM `User` WHERE Vorname=?", (some_name,)) 

for some_name in cur: 
    print(f"First name: {some_name}, ")