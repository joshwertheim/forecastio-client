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

    wind_measurements = { 'us': 'MPH', 'si': 'MPS', 'ca': 'KPH' }
    temperature_measurements = { 'us': 'F', 'si': 'C' }
    default_units = 'us'
    measurement_units = None

    def __init__(self):
        """Inits FCClient with DarkSky API key."""
        super(FCClient, self).__init__()
        self.api_key = os.environ.get('DARKSKYAPI')

    def current_forecast_response(self, coordinates, units):
        try:
            self.current_coordinates = coordinates
            send_url = 'https://api.darksky.net/forecast/{}/{},{}'.format(self.api_key, coordinates.get('lat'), coordinates.get('lon'))
            if units:
                self.measurement_units = units
                send_url += "?units={}".format(units)
            r = requests.get(send_url)
            j = json.loads(r.text)
            self.current_forecast = j
            self.currently = self.current_forecast.get('currently')
        except Exception, e:
            print e

    def current_data(self):
        if self.measurement_units is None:
            self.measurement_units = self.default_units
        print "Current weather:", self.current_summary()
        if self.measurement_units == 'ca' or self.measurement_units == 'si':
            temp_units = self.temperature_measurements['si']
        else:
            temp_units = self.temperature_measurements['us']
        print "Current temp:", self.current_temperature(), temp_units
        print "Current wind speed:", self.current_wind_speed(), self.wind_measurements[self.measurement_units]

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
