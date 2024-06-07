import requests
from requests import Response

import configuration

import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


response = post_new_order(data.order_body)

print(response.status_code)

print(response.json()) # Создаю пользователя чтобы получить трекномер

def get_order(track_number):
    response = requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER, params={'t': track_number})
    return response
print(response.status_code)
print(response.json())