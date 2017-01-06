import json

import requests
from geopy.geocoders import Nominatim

class Location(object):
    """Create a Location instance

    Use to get current coordinates of the device running
    this code via a geolocation service or zipcode
    """

    def current_position_coordinates(self):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        return { 'lat': lat, 'lon': lon }

    def coordinates_from_zipcode(self, zipcode):
        geolocator = Nominatim()
        location = geolocator.geocode(zipcode).raw
        lat = location[u'lat']
        lon = location[u'lon']
        return { 'lat': lat, 'lon': lon }