import requests
import time

def access():
    print("logged...")
    cnt = 0
    while True:
        cnt += 1
        requests.get("https://salty-lake-16271.herokuapp.com/")
        print("Logged!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(cnt)
        time.sleep(10)