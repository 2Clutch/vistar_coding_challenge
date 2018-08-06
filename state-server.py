import json

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8080

with open("states.json") as f:
    data = json.load(f)
    print(data)
