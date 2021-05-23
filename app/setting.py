from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


class DevelopmentConfig():
    HOSTNAME = '123.56.117.178'
    PORT = '3306'
    DATABASE = 'test_helper'
    USERNAME = 'root'
    PASSWORD = '666666'

    SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
    # 调度器开关
    SCHEDULER_API_ENABLED = True
    # -------持久化配置---------
    # job存储位置
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    }
    # 线程池配置
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 10}
    }