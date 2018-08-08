import json
from urllib.parse import urlparse, parse_qs
from shapely.geometry import Polygon as pol, Point as p
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8080

LO = 0  # longitude
LA = 1  # latitude

with open("states.json") as f:
    data = json.load(f)


def search(cord):
    if cord:
        point = p(cord[LO], cord[LA])
        for state in data:
            polygon = pol(state['border'])
            if polygon.contains(point):
                return state['state']


class RequestHandler(BaseHTTPRequestHandler):
    def do_get(self):
        input_query = urlparse(self.path).query
        if input_query:
            query_lo_la = parse_qs(input_query)
            if 'latitude' in query_lo_la and 'longitude' in query_lo_la:
                self.send_response(200)
                points = [float(query_lo_la['longitude'][0]), float(query_lo_la['latitude'][0])]
                state_output = search(points)
                if state_output:
                    return state_output['state']


if __name__ == '__main__':
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = HTTPServer(server_address, RequestHandler)
    try:
        print("Serving at: " + HOST_NAME + ":" + str(PORT_NUMBER))
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server Stopped.")
