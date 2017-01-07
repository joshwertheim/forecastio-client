import argparse

from location import Location
from forecast import FCClient

test = 0

def setup(**kwargs):
    loc = Location()

    if kwargs['geolocation']:
        position_coordinates = loc.current_position_coordinates()
    elif kwargs['zipcode'] is not None:
        position_coordinates = loc.coordinates_from_zipcode(kwargs['zipcode'])
    else:
        return

    fcclient = FCClient()
    fcclient.current_forecast_response(position_coordinates, kwargs.get('units_type'))
    fcclient.current_data(lat=position_coordinates['lat'], lon=position_coordinates['lon'])

def main():
    parser = argparse.ArgumentParser(description="What's the weather?")
    parser.add_argument('-geolocation', action="store_true")
    parser.add_argument('-zipcode', action="store", dest="zipcode")
    parser.add_argument('-units', action="store", dest="units")
    commands = parser.parse_args()
    setup(geolocation=commands.geolocation, zipcode=commands.zipcode, units_type=commands.units)

if __name__ == '__main__':
    main()