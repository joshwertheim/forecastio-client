import sys
import json

import requests

class FCClient(object):
    """docstring for FCClient"""

    def __init__(self):
        super(FCClient, self).__init__()
        self.api_key = 'd444457a7e57fca2009608bcce9df40f'

    def current_forecast(self, coordinates):
        try:
            send_url = 'https://api.darksky.net/forecast/{}/{},{}'.format(self.api_key, coordinates.get('lat'), coordinates.get('lon'))
            r = requests.get(send_url)
            j = json.loads(r.text)
        except Exception, e:
            print e