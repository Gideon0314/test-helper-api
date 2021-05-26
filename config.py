# -*- coding: UTF-8 -*-
import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')


class Config():

    DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    HOST_NAME = os.environ.get('MYSQL_HOSTNAME')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{HOST_NAME}:{MYSQL_PORT}/{MYSQL_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10000
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    }
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 10}
    }
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    INQUIRY_EMAIL = ''
    INQUIRY_EMAIL_PW = ''
    INQUIRY_EMAIL_LIST = []
    # 日志输出到控制台还是日志文件中
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT', 'false').lower() in ['true', 'on', '1']

