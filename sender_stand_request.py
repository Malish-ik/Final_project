import data
import configuration
import requests


def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body, headers=data.headers)
    return response.json()['track']


#response = post_new_order(data.order_body);

#print(post_new_order(data.order_body))
#print(response.json())

def get_order_status_code():
    track_number = post_new_order(data.order_body)
    response = requests.get((configuration.URL_SERVICE + configuration.GET_ORDER), params={'t': track_number})
    return response.status_code


#print(get_order_id())