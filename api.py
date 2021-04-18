# Module Imports
import mariadb
import sys
import secrets

# Connect to MariaDB Platform
def connect_to_DB():
    try:
        conn = mariadb.connect(
            user=secrets.Database_user,
            password=secrets.Database_pw,
            host="159.hosttech.eu",
            port=3306,
            database="IOXCoding"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    # Get Curso
    
    

def adding_data(temperature, humidity):
    conn = connect_to_DB()
    cur = conn.cursor()
    try: 
        cur.execute("INSERT INTO Test_Data (temperature,humidity) VALUES (?, ?)", (temperature,humidity)) 
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit() 
