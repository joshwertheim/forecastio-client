import json

import requests

class Location(object):
    """docstring for Location"""

    def current_position_coordinates(self):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']

        return { 'lat': lat, 'lon': lon }