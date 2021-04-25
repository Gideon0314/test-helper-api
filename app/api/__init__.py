# -*- coding: UTF-8 -*-
from flask import Blueprint


bp = Blueprint('web', __name__, template_folder='templates')


from . import project
from . import test_job
from . import login
from . import user
from . import task
from . import ping
from . import build_history
