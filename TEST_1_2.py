import requests

import configuration

def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER)


response = get_order()


print(response.status_code)
print(response.json())