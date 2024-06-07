import requests
import configuration
import data

def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)
    return response

def get_order(track_number):
    response = requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER, params={'t': track_number})
    return response

def test_track_order():

    response = post_new_order(data.order_body)
    assert response.status_code == 201
    #
    track_number = response.json()['track']

    response = get_order(track_number)

    assert response.status_code == 200
    print(response.status_code)

test_track_order()
