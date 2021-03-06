# DarkSky Client (for forecast.io)

Acts as a minimal client for the DarkSky weather forecast API.

## Getting Started

This program requires the use of an API token from DarkSky. Register on the [DarkSky development website](https://darksky.net/dev/) in order to obtain one.

You may clone this repo using: 

`https://github.com/joshwertheim/forecastio-client.git`

Next, `cd` to this repo and make sure all required third-party modules are installed as they are pre-requisites for running this program: 

`pip install -r requirements.txt`

## Usage

There are currently two ways to use this program:

Run `python modules/core.py -geolocation` and the program will ping [http://freegeoip.net](http://freegeoip.net) for your current geolocation.

Run `python modules/core.py -zipcode 94107` and the program will use the *geopy* module to obtain coordinates for your given zipcode, and then retrieves weather forecast data for that location.

At present, the output should look something like this:

```
[01:11:09] joshuawertheim@Joshuas-Air: ~/Development/python/forecastio-client  > python modules/core.py -geolocation
Current weather: Light Rain
Current temp: 46.69 F
Current wind speed: 10.28 MPH

[01:51:53] joshuawertheim@Joshuas-Air: ~/Development/python/forecastio-client  > python modules/core.py -zipcode 94107
SF (Mission Creek), California, US

Current weather: Overcast
Current temp: 45.93 F
Current wind speed: 9.34 MPH

[01:11:30] joshuawertheim@Joshuas-Air: ~/Development/python/forecastio-client  > python modules/core.py -zipcode 94107 -units si
SF (Mission Creek), California, US

Current weather: Light Rain
Current temp: 7.73 C
Current wind speed: 4.15 MPS

[01:12:06] joshuawertheim@Joshuas-Air: ~/Development/python/forecastio-client  > python modules/core.py -zipcode 94107 -units ca
SF (Mission Creek), California, US

Current weather: Light Rain
Current temp: 7.81 C
Current wind speed: 14.39 KPH
```

## Notes

This is just something quick that I whipped up in the middle of the night so it's not perfect and is very minimal. I might be adding to it as I have some ideas of what I would like to do.

Feel free to send a PR for anything interesting! Thanks!
