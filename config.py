# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
a = load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')



SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# class Config(object):
#     pass

HOSTNAME = '123.56.117.178'
PORT = '3306'
DATABASE = 'test_helper'
USERNAME = 'root'
PASSWORD = '666666'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 1000


# SESSION_TYPE = 'sqlalchemy'

INQUIRY_EMAIL = 'tjd0314@126.com'
INQUIRY_EMAIL_PW = 'SQDXTUHPZZORDIXL'
INQUIRY_EMAIL_LIST = [
    'gideon_tao0119@chinakej.top',
]
