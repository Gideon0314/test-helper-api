# -*- coding: UTF-8 -*-


# -*- coding: UTF-8 -*-
from flask import request, render_template, flash, redirect, url_for, abort, jsonify
# from app.froms.project import ProjectForm
from app.libs.test_email_inquiry import email_inquiry
from app.models.project import Project
from app.models.api_docs import ApiDocs
from app.models import db
from . import bp


@bp.route('/test/email_inquiry', methods=['GET'])
def test_email_inquiry():
    """ 测试 """
    email_inquiry()
    return ("", 204)
