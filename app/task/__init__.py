from flask_apscheduler import APScheduler
# 实例APScheduler定时任务
from app.libs.add_task import add_task

scheduler = APScheduler()

def add_job(**kwargs):
    response = {'status': False}
    try:
        scheduler.add_job(**kwargs)
        response['status'] = True
        response['msg'] = "job[%s] addjob success!" % id
        add_task(**kwargs)
        print("添加一次性任务成功---[ %s ] " % id)
    except Exception as e:
        response['msg'] = str(e)


def pause_job():
    pass

def resume_job():
    pass