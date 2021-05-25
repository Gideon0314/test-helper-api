from apscheduler.schedulers.gevent import GeventScheduler
from flask_apscheduler import APScheduler
# 实例APScheduler定时任务

# scheduler = APScheduler()
scheduler = GeventScheduler()
