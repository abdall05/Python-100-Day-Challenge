import requests
import os
from sms_sender import send_sms

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
API_URL = 'https://api.openweathermap.org/data/2.5/forecast'
CITY = "passau"
LATITUDE = 48.5665
LONGITUDE = 13.43122
COUNT = 5  # number of timestamps (each 3 hour from now)


def get_weather_data(latitude=LATITUDE, longitude=LONGITUDE):
    parameters = {

        'lat': latitude,
        'lon': longitude,
        'cnt': COUNT,
        'appid': WEATHER_API_KEY,

    }

    response = requests.get(API_URL, params=parameters)
    response.raise_for_status()
    return response.json()


def extract_weather_ids(weather_data):
    weather_ids = []
    if weather_data == {}:
        return weather_ids
    for weather_info_per_3_hours in weather_data['list']:
        weather_ids.append(weather_info_per_3_hours['weather'][0]['id'])
    return weather_ids


def need_umbrella(weather_ids):
    for weather_id in weather_ids:
        if weather_id < 700:
            return True
    return False

if __name__ == "__main__":
    try:
        data = get_weather_data()
    except Exception as e:
        data = {}
        print(e)
    weather_id_list = extract_weather_ids(data)
    if  need_umbrella(weather_id_list):
        send_sms()
