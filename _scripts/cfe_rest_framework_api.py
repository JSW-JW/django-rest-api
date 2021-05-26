import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"


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

do(method='delete', data={"id": 500})