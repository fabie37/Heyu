import requests
from time import sleep

code = "15634"

usr_input= input("Press Enter to Start:")
while (usr_input != "stop"):
    usr_input = input("Send a notification to?")
    api_url = "http://localhost:5000/notification"
    body = {"code":code}
    requests.post(api_url, json=body)