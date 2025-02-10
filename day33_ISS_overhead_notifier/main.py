import time

import requests
import datetime as dt
from my_notifier import notify_me

MY_LATITUDE = 48.566734
MY_LONGITUDE = 13.431947
MY_POSITION = (MY_LATITUDE, MY_LONGITUDE)
MY_TZID = "Europe/Berlin"

ISS_API = "http://api.open-notify.org/iss-now.json"
DAY_TIME_API = "https://api.sunrise-sunset.org/json"




def get_iss_position():
    response = requests.get(ISS_API)
    data = response.json()
    return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])


def get_sunrise_and_sunset_time():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "tzid": MY_TZID,
        "formatted": 0
    }
    response = requests.get(DAY_TIME_API, params=parameters)

    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunrise_time_str = sunrise.split("T")[1].split("+")[0]
    sunrise_time = dt.datetime.strptime(sunrise_time_str, "%H:%M:%S").time()
    sunset = data["results"]["sunset"]
    sunset_time_str = sunset.split("T")[1].split("+")[0]
    sunset_time = dt.datetime.strptime(sunset_time_str, "%H:%M:%S").time()
    return sunrise_time, sunset_time


def is_near_me(object_latitude, object_longitude):
    return abs(object_latitude - MY_LATITUDE) <= 5 and abs(object_longitude - MY_LONGITUDE) <= 5


def is_night(sunrise_time, sunset_time):
    return not sunrise_time <= dt.datetime.now().time() <= sunset_time


while True:
    sunrise_time, sunset_time = get_sunrise_and_sunset_time()
    iss_latitude, iss_longitude = get_iss_position()
    print(f"{iss_latitude}, {iss_longitude}")
    print(f"{sunrise_time}, {sunset_time}")
    if is_near_me(iss_latitude, iss_longitude) and is_night(sunrise_time, sunset_time):
        try:
            notify_me()
        except:
            print("Something went wrong")
    time.sleep(3600)
