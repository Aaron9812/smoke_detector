# Module Imports
import googlemaps
import mariadb
import sys
import secrets
import time, random
import requests

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

def adding_random_data():
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
            
    con.close()

def adding_data(device_id, temp,co2, lpg, smoke):
    con = connect_to_DB()
    cur = con.cursor()

    try: 
        cur.execute("INSERT INTO data (temperature, co, lpg, smoke, device_id) VALUES (?, ?, ?, ?, ?)", (temp,co2, lpg, smoke, device_id)) 
    except mariadb.Error as e: 
        print(f"Error: {e}")

    con.commit()
    con.close()

def lichtan():
    request = requests.post("https://maker.ifttt.com/trigger/licht_an/with/key/"+ secrets.ifttt_key)

def lichtaus():
    request = requests.post("https://maker.ifttt.com/trigger/licht_aus/with/key/"+ secrets.ifttt_key)

def get_lat_long(address):
    gmaps = googlemaps.Client(key=secrets.google_Maps_key)

    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]
    return lat,lng
if __name__ == "__main__":
    lichtaus()
    