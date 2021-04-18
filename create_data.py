import api
import random
import time

def create_data():
    temp = random.uniform(1.5, 35.5)
    humidity = random.uniform(0.05, 0.95)
    api.adding_data(temp, humidity)
    time.sleep(1)

while True:
    create_data()