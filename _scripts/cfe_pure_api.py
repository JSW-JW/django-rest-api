import json
import requests  # http requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"


def get_list(id=None): #--> Lists all this out
    data = {}
    if id is not None:
        data = {
            "id": id
        }

    r = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))

    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def create_update():
    new_data = {
        'user': 1,
        "content": "validate create_update content"
    }

    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def create_update_not_allowed():
    data_empty = {
        'user': '1',
        'content': '',
    }

    r = requests.post(BASE_URL + ENDPOINT + "1/", data=json.dumps(data_empty))
    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def do_obj_update():
    new_data = {
        "id": 2,
        "content": "how about now?"
    }
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def do_obj_delete():
    new_data = {
        "id": 2,
        "content": "Now I am trying to delete item through ListAPIEndpoint"
    }

    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


print(get_list())
