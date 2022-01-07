import requests
from time import sleep
from random import randint

code = "15634"
responses = ["Hi", "hey", "what's up?", "heya!"]

# 1) Connect to API and register self
api_url = "http://localhost:5000"
body = {"code": code}
response = requests.post(api_url + "/heyu", json=body)

if "error" in response:
    print("Well shit.")
    exit()

# 2) Poll server for notifications
while(True):
    sleep(1)
    response = requests.get(api_url + "/notification", json=body).json()
    if "notification" in response and response["notification"] != False:
        print(responses[randint(0, len(responses)-1)])