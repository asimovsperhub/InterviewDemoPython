import json

import requests

add = {
    "value_array": [
        {"value": 12},
        {"value": 18},
        {"value": 10}
    ]
}
chat = {
    "msg": "再见"
}

data = json.dumps(chat)
rep = requests.post('http://120.79.245.107:3112/chat', data=data)

print(json.loads(rep.text))
