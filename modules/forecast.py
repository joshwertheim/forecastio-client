import os, sys
import json

import requests

class FCClient(object):
    """Create a FCClient instance

    Use this client class to access the DarkSky (Forecast.io) weather
    forecast API (1000 free calls per day)

    Attributes:
        api_key: Used to access the DarkSky API
    """

    def __init__(self):
        """Inits FCClient with DarkSky API key."""
        super(FCClient, self).__init__()
        self.api_key = os.environ.get('DARKSKYAPI')

    def current_forecast_response(self, coordinates):
        try:
            self.current_coordinates = coordinates
            send_url = 'https://api.darksky.net/forecast/{}/{},{}'.format(self.api_key, coordinates.get('lat'), coordinates.get('lon'))
            r = requests.get(send_url)
            j = json.loads(r.text)
            self.current_forecast = j
            self.currently = self.current_forecast.get('currently')
        except Exception, e:
            print e

    def current_data(self):
        print "Current weather:", self.current_summary()
        print "Current temp:", self.current_temperature(), 'F'
        print "Current wind speed:", self.current_wind_speed(), 'MPH'

    def current_summary(self):
        return self.currently.get('summary')

    def current_temperature(self):
        return self.currently.get('temperature')

    def current_dewpoint(self):
        return self.currently.get('dewPoint')

    def current_humidity(self):
        return self.currently.get('humidity')

    def current_wind_speed(self):
        return self.currently.get('windSpeed')

    def refresh(self):
        self.current_forecast_response(self.current_coordinates)
