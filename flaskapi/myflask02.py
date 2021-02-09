#!/usr/bin/python3
"""Mimic http://api.open-notify.org/astros.json"""

# An object of Flask class is our WSGI application
from flask import Flask

# lets us return JSON attachments
from flask import jsonify

# we will return this data by our API
# in production, this data might come from a database
MYDATA = {"message": "success", "number": 3, "people": [{"craft": "ISS", "name": "Sergey Ryzhikov"}, {"craft": "ISS", "name": "Kate Rubins"}, {"craft": "ISS", "name": "Sergey Kud-Sverchkov"}]}

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

@app.route("/astros", methods = ["GET"])   # "respond to HTTP GET /astros"
def astros():
   return jsonify(MYDATA)   # return 200+JSON

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

