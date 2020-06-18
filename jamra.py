"""
Jamra - Just Another Mock Rest API

Simple RestAPI Server with mocked data
"""

import json
from flask import Flask

jamra = Flask(__name__)


@jamra.route("/")
def base_url():
    """
    GET /
    Endpoint for the base url
    """
    return json.loads('{"message": "Try with /data", "success": false}')

@jamra.route("/ping")
def ping():
    """
    GET /ping
    Endpoint for pinging
    """
    return json.loads('{"message": "pong", "success": true}')

@jamra.route("/data")
def get_data():
    """
    GET /data
    Endpoint for getting the mocked data
    """
    try:
        with open('./data.json') as data_file:
            return json.load(data_file)
    except:
        data_json = json.loads('{"message": "Error with file data.json", "success": false}')
    return data_json

@jamra.route("/data", methods=['POST'])
def post_data():
    """
    POST /data
    Endpoint for posting mocked data
    """
    return json.loads('{"success":true, "message":"Data created (but not really)" }')

if __name__ == "__main__":
    jamra.run(debug=True)
