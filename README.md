# DarkSky Client (for forecast.io)

Acts as a minimal client for the DarkSky weather forecast API.

## Getting Started

This program requires the use of an API token from DarkSky. Register on the [DarkSky development website](https://darksky.net/dev/) in order to obtain one.

You may clone this repo using: 

```https://github.com/joshwertheim/forecastio-client.git```

Next, `cd` to this repo and make sure all required third-party modules are installed as they are pre-requisites for running this program: 

```pip install -r requirements.txt```

## Usage

There are currently two ways to use this program:

Run ```python modules/core.py``` and the program will ping [http://freegeoip.net](http://freegeoip.net) for your current geolocation.

Run ```python modules/core.py -zipcode 94107``` and the program will use the *geopy* module to obtain coordinates for your given zipcode, and then retrieves weather forecast data for that location.

At present, the output should look something like this:

```
[13:08:15] joshuawertheim@Joshuas-Air: ~/Development/python/forecastio-client  > python modules/core.py
Current weather: Partly Cloudy
Current temp: 46.6 F
Current wind speed: 7.26 MPH

[03:46:36] joshuawertheim@Joshuas-Air: ~/Development/python/forecastio-client  > python modules/core.py -zipcode 94107
Current weather: Partly Cloudy
Current temp: 46.75 F
Current wind speed: 7.43 MPH
```

## Notes

This is just something quick that I whipped up in the middle of the night so it's not perfect and is very minimal. I might be adding to it as I have some ideas of what I would like to do.

Feel free to send a PR for anything interesting! Thanks!
