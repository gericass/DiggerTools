import requests
import time
from datetime import datetime

def access():
    print("logged...")
    while True:
        requests.get("https://salty-lake-16271.herokuapp.com/")
        print("Logged!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(datetime.now())
        time.sleep(10)