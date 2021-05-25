import json
from datetime import datetime
from datetime import date
import requests


def my_job():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d855bbd4-eacf-4d1a-8da4-ab2d71ef250e'
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content":f"{date.today()}定时任务测试\n"
            }
        }
    r = requests.post(url, json.dumps(data))
    if r.status_code == 200:
        print('消息发送成功')
