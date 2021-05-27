import json
from datetime import datetime
import requests
from app.extensions import scheduler


# @scheduler.task(
#     "interval",
#     id="1",
#     seconds=10,
#     max_instances=1,
# )
def my_job():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cb47d771-e6fd-49e4-9df7-39ff1eb634e2'
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content":f"{datetime.now()}定时任务测试\n"
            }
        }
    r = requests.post(url, json.dumps(data))
    if r.status_code == 200:
        print('消息发送成功')


# @scheduler.task(
#     "interval",
#     id="2",
#     seconds=10,
#     max_instances=1,
# )
# def task1():
#     """Sample task 1.
#     Added when app starts.
#     """
#     print("running task 1!")  # noqa: T001
#     # oh, do you need something from config?
#     with scheduler.app.app_context():
#         print(scheduler.app.config)  # noqa: T001
