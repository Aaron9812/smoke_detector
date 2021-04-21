# Module Imports
import mariadb
import sys
import secrets
import time, random

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
    
    

def adding_data():
    con = connect_to_DB()
    cur = con.cursor()

    for i in range(600):
        temp = random.uniform(1.5, 35.5)
        humidity = random.uniform(0.05, 0.95)
        time.sleep(1)
        try: 
            cur.execute("INSERT INTO Test_Data (temperature,humidity) VALUES (?, ?)", (temp,humidity)) 
        except mariadb.Error as e: 
            print(f"Error: {e}")
        
        if i % 100 == 0:
            con.commit()
            print("Commited")
    con.close()

if __name__ == "__main__":
    adding_data()