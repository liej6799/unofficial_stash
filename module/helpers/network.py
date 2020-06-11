import requests

headers = {'Content-Type': 'application/json;charset=utf-8',
           'x-client-identifier': 'webapp@2.29.0'}


def post_data(path, data):
    r = requests.post(path, headers=headers, data=data)
    return r.json()
