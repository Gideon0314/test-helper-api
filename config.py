# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

DEBUG = os.environ.get('FLASK_DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY')

# class Config(object):
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

SCHEDULER_API_ENABLED = True
# 定时任务存储位置
SCHEDULER_JOBSTORES = {
    'default': SQLAlchemyJobStore(SQLALCHEMY_DATABASE_URI)
}
SCHEDULER_TIMEZONE = 'Asia/Shanghai'

# SESSION_TYPE = 'sqlalchemy'

INQUIRY_EMAIL = ''
INQUIRY_EMAIL_PW = ''
INQUIRY_EMAIL_LIST = [
    'gideon_tao0119@chinakej.top',
]
