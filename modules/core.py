import argparse

from location import Location
from forecast import FCClient

def setup(zipcode=None):
    loc = Location()
    if not zipcode:
        position_coordinates = loc.current_position_coordinates()
    else:
        position_coordinates = loc.coordinates_from_zipcode(zipcode)

    fcclient = FCClient()
    fcclient.current_forecast_response(position_coordinates)
    fcclient.current_data()

def main():
    parser = argparse.ArgumentParser(description="What's the weather?")
    parser.add_argument('-zipcode', action="store", dest="zipcode")
    commands = parser.parse_args()
    if commands.zipcode:
        setup(commands.zipcode)
    else:
        setup()

if __name__ == '__main__':
    main()