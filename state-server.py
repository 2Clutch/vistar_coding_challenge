import json
import argparse
from flask import Flask
from shapely.geometry import Polygon as pol, Point as p

app = Flask(__name__)

with open("states.json") as f:
    data = json.load(f)


@app.route('/', methods=['POST'])
def search(cord):
    parser = argparse.ArgumentParser()
    lon = parser.add_argument("longitude", type=int)
    lat = parser.add_argument("latitude", type=int)
    args = parser.parse_args()

    if cord:
        point = p(cord[args[lon]], cord[args[lat]])
        for state in data:
            polygon = pol(state['border'])
            if polygon.contains(point):
                return state['state']


if __name__ == '__main__':
    app.run()
