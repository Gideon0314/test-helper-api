# -*- coding: UTF-8 -*-
from flask import  Blueprint
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

bp = Blueprint('web', __name__)

from . import project
from . import test_job


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    '''最常用的错误 400：错误的请求'''
    return error_response(400, message)