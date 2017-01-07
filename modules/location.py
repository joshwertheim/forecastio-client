import json

import requests
from geopy.geocoders import Nominatim

class Location(object):
    """Create a Location instance

    Use to get current coordinates of the device running
    this code via a geolocation service or zipcode
    """

    def __init__(self):
        super(Location, self).__init__()
        self.geolocator = Nominatim()

    def current_position_coordinates(self):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        return { 'lat': lat, 'lon': lon }

    def coordinates_from_zipcode(self, zipcode):
        location = self.geolocator.geocode(zipcode).raw
        lat = location[u'lat']
        lon = location[u'lon']
        return { 'lat': lat, 'lon': lon }

    def location_from_coordinates(self, lat, lon):
        position = '{},{}'.format(lat, lon)
        location = self.geolocator.reverse(position)
        city = location.raw[u'address'][u'city']
        neighborhood = location.raw[u'address'][u'neighbourhood']
        state = location.raw[u'address'][u'state']
        country = location.raw[u'address'][u'country_code']
        return { 'city': city, 'neighborhood': neighborhood, 'state': state, 'country': country }
