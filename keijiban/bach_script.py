import requests
import time

def access():
    print("logged...")
    while True:
        requests.get("https://salty-lake-16271.herokuapp.com/")
        print("Logged!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(10)