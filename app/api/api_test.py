# -*- coding: UTF-8 -*-
from flask import request, render_template, flash, redirect, url_for, abort
from app.models.project import Project
from app.models.api_docs import ApiDocs
from app.models import db
from app import bp
# from back_end.app.froms.project import ProjectForm


@bp.route('/api_docs/list/<int:page>')
def project_list(page):
    """ 项目列表 """

    # 页码上限
    page_size = 10
    # 查询
    name = request.args.get('name', '')
    if name:
        page_data = Project.query.filter_by(name=Project.name.contains(name), is_valid=True).paginate(page=page, per_page=page_size)
    else:
        page_data = Project.query.filter_by(is_valid=True).paginate(page=page, per_page=page_size)
    return render_template('project/index.html', page_data=page_data)
