# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import json

import requests

url = "http://localhost:81/api/user/login"
# headers = {
#     "Content-Type": "application/json"
# }
r = requests.post(url=url,auth=('admin', '666666'))
print(r)
