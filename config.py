# -*- coding: UTF-8 -*-
import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')


DEBUG = os.environ.get('FLASK_DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY')

class Config():
#     pass
    # HOSTNAME = ''
    HOSTNAME = '123.56.117.178'
    PORT = '3306'
    DATABASE = 'test_helper'
    USERNAME = 'root'
    PASSWORD = '666666'

    SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10000

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

    SCHEDULER_TIMEZONE = 'Asia/Shanghai'

    # SESSION_TYPE = 'sqlalchemy'

    INQUIRY_EMAIL = ''
    INQUIRY_EMAIL_PW = ''
    INQUIRY_EMAIL_LIST = [
        'gideon_tao0119@chinakej.top',
    ]
