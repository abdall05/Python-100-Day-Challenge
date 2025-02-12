import datetime as dt
import os

from dotenv import load_dotenv, find_dotenv

import requests

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

PIXE_USER_ENDPOINT = "https://pixe.la/v1/users"


def create_user(username, token):
    user_params = {
        'token': token,
        'username': username,
        'agreeTermsOfService': "yes",
        'notMinor': "yes"
    }
    requests.post(PIXE_USER_ENDPOINT, json=user_params)


def create_graph(username, token, graph_id, name, data_type, unit):
    graph_endpoint = f"{PIXE_USER_ENDPOINT}/{username}/graphs"
    graph_params = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": data_type,
        "color": "ichou"

    }

    headers = {
        "X-USER-TOKEN": token
    }

    requests.post(graph_endpoint, json=graph_params, headers=headers)


def create_today_pixel(username, token, graph_id, quantity):
    date = dt.datetime.today().strftime("%Y%m%d")
    graph_endpoint = f"{PIXE_USER_ENDPOINT}/{username}/graphs"
    pixel_endpoint = f"{graph_endpoint}/{graph_id}"
    pixel_graph_params = {
        "date": date,
        "quantity": quantity

    }
    headers = {
        "X-USER-TOKEN": token
    }
    requests.post(url=pixel_endpoint, json=pixel_graph_params, headers=headers)


def update_pixel(username, token, graph_id, date, nex_pixel_data):
    graph_endpoint = f"{PIXE_USER_ENDPOINT}/{username}/graphs"
    pixel_endpoint = f"{graph_endpoint}/{graph_id}"
    pixel_update_endpoint = f"{pixel_endpoint}/{date}"
    headers = {
        "X-USER-TOKEN": token
    }

    requests.put(url=pixel_update_endpoint, json=nex_pixel_data, headers=headers)


def delete_pixel(username, token, graph_id, date):
    graph_endpoint = f"{PIXE_USER_ENDPOINT}/{username}/graphs"
    pixel_endpoint = f"{graph_endpoint}/{graph_id}"
    pixel_delete_endpoint = f"{pixel_endpoint}/{date}"
    headers = {
        "X-USER-TOKEN": token
    }
    requests.delete(pixel_delete_endpoint, headers=headers)
