from location import Location
from forecast import FCClient

def setup():
    loc = Location()
    position_coordinates = loc.current_position_coordinates()

    fcclient = FCClient()
    fcclient.current_forecast_response(position_coordinates)
    fcclient.current_data()

def main():
    setup()

if __name__ == '__main__':
    main()