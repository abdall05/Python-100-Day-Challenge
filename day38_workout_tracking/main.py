import os

import requests
import datetime as dt
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_API_ID = os.getenv("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

SHEETY_API_ENDPOINT = "https://api.sheety.co/ccaa4436f9d2a7bf09723a06d8d6d57c/myWorkouts/workouts"
SHEETY_BASIC_AUTHENTICATION = os.getenv("SHEETY_BASIC_AUTHENTICATION")

SEET_URL = "https://docs.google.com/spreadsheets/d/1fYxSaG8jeRKNLN_nRFYZvFhP13eO9NWDdqZMbAPgZ8A/edit?usp=sharing"

query = input("What exercises did you do today?")
nutritionix_request_headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}
nutritionix_request_body = {
    "query": query,
}
nutritionix_response = requests.post(url=API_ENDPOINT, json=nutritionix_request_body,
                                     headers=nutritionix_request_headers)
nutritionix_response.raise_for_status()
sheety_request_headers = {
    "Authorization": SHEETY_BASIC_AUTHENTICATION,
}
for exercise in nutritionix_response.json()["exercises"]:
    exercise_name = exercise["user_input"]
    date = dt.date.today().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%H:%M:%S")
    duration = f"{exercise["duration_min"]}min"
    calories = exercise["nf_calories"]
    sheety_row_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories,
        }
    }
    print(sheety_row_data["workout"])
    post_request = requests.post(url=SHEETY_API_ENDPOINT, json=sheety_row_data, headers=sheety_request_headers)
    post_request.raise_for_status()
