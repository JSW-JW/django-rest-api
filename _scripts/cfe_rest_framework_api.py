import requests
import json

import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path_1 = os.path.join(os.getcwd(), "cute-dog.jpg")
image_path_2 = os.path.join(os.getcwd(), "beautiful-woman.jpg")


def do_img_post(method='post', data={}, img_path=None, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path_1, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


def do_img_update(method='post', data={}, img_path=None, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path_2, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


# do_img_post(method='post', data={"user": 1}, img_path=image_path_1, is_json=False)

do_img_update(method='put',
              data={'user': 1, 'id': 9, 'content': 'some updated content'},
              img_path=image_path_2,
              is_json=False)


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


# do(data={"id": 7})

# do(method='put', data={"id": 7, "content": "put update by requests module", "user": 1})

# do(method='post', data={"content": "instance created by requests module", "user": 1})

# do(method='delete', data={"id": 500})