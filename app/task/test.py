import json
from datetime import datetime
from datetime import date
import requests


def my_job():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cb47d771-e6fd-49e4-9df7-39ff1eb634e2'
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content":f"{date.today()}定时任务测试\n"
            }
        }
    r = requests.post(url, json.dumps(data))
    if r.status_code == 200:
        print('消息发送成功')
