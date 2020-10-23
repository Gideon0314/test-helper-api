# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import json

import requests

url = "http://127.0.0.1:81/api/tokens"
headers = {
    "Content-Type": "application/json"
}
r = requests.post(url=url,auth=('admin', '666666'),headers=headers)
print(r)
