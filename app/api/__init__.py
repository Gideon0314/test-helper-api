# -*- coding: UTF-8 -*-
from flask import Blueprint


bp = Blueprint('web', __name__)


from . import project, test_job, login, user, task
