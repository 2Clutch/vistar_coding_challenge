import json
from shapely.geometry import Polygon as pol, Point as p


HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8080

LO = 0  # longitude
LA = 1  # latitude

with open("states.json") as f:
    data = json.load(f)
    print(data)


def search(cord):
    if cord:
        point = p(cord[LO], cord[LA])
        for state in data:
            polygon = pol(state['border'])
            if polygon.contains(point):
                return state['state']
