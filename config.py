# -*- coding: UTF-8 -*-
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
a = load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

DEBUG = os.environ.get('FLASK_DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY')

# class Config(object):
#     pass

HOSTNAME = ''
PORT = '3306'
DATABASE = 'test_helper'
USERNAME = 'root'
PASSWORD = '666666'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 10000


# SESSION_TYPE = 'sqlalchemy'

INQUIRY_EMAIL = ''
INQUIRY_EMAIL_PW = ''
INQUIRY_EMAIL_LIST = [
    'gideon_tao0119@chinakej.top',
]
