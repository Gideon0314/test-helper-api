# -*- coding: UTF-8 -*-
import json
import re
from functools import wraps
from datetime import datetime
import requests
from app import db
from app.api.errors import bad_request
from app.models.task import Task


# def next_run_time(task_id):
#     data = scheduler.get_job(task_id)
#     print(data)
#     nrt = re.findall('', data)
#     return nrt


def add_task(data):
    """ 项目添加 """
    if Task.query.filter_by(task_id=data.get('task_id', None), is_valid=True).first():
        return bad_request('定时任务ID已存在')
    data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_data = Task()
    task_data.from_dict(data)
    db.session.add(task_data)
    db.session.commit()


def test_aps():
    data = {
	"task_id": "2",
    "task_name": "每日询盘监测",
    "remark": "定时发送表单及邮件询盘",
    "env": "3",
	"interval_time": 10,
	"trigger_type": "interval",
    "status": 1
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
    }
    url = 'http://localhost:81/api/addCron'
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        print(r.json)


def task(func):
    @wraps(func)  # 使用本条命令可以让func函数返回其本身的函数名等。
    def import_task(*args, **kwargs):
            print(func.__name__)
            print(func.__doc__)
            print('定时任务去重新增')
            ret = func(*args,**kwargs)
            return ret
    return import_task


@task
def func(*args, **kwargs):
    '''定时任务1'''
    print('this is a test')


if __name__ == '__main__':
    # func('ok')
    test_aps()
