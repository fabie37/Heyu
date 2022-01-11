from flask import Flask, request, jsonify
from queue import Queue

import requests

server = Flask(__name__)

codes = {
    "1234",
}

notifications = {
    "1234" : Queue(),
}

notifications["1234"].put("Hey")

# GET: notification
# Description: Checks database for a notification from heyu friend
# expected param: 
#           "code" : <str>      Identify heyu code
@server.get("/notification/<code>")
def get_notification(code):
    if request.is_json:
        req = request.get_json()
        if "code" in req:
            code = req["code"]
            if code in notifications: 
                if notifications[code].empty():
                    return {"notification": False}, 201
                return {"notification": notifications[code].get()}, 203
            return {"error":" Bad Request"}, 400
        return {"error":" Bad Request"}, 400
    return {"error":"Request must be json"}, 415

# POST: notification
# Description: Puts a notification into database
# expected body: 
#           "code" : <str>      Identify heyu code
@server.post("/notification")
def post_notification():
    if request.is_json:
        req = request.get_json()
        if "code" in req:
            code = req["code"]
            if code in notifications:
                notifications[code].put("hey")
                return {"success": True}, 201
            return {"error": "Heyu not found"}, 400
        return {"error": "Please enter code"}, 400
    return {"error":"Request must be json"}, 415

# POST: heyu
# Description: Adds a heyu to the database
# expected body:
#           "code" : <str>      New heyu to add
@server.post("/heyu")
def post_heyu():
    if request.is_json:
            req = request.get_json()
            code = req["code"]
            notifications[code] = Queue()
            return {"success": True}, 200
    return {"error":"Request must be json"}, 415  
