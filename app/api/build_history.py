# -*- coding: UTF-8 -*-
from app.models import db
from app.api import bp
from flask import request, jsonify
from datetime import datetime
from app.api.errors import bad_request
from app.models.build_history import BuildHistory
from app.models.project import Project


@bp.route('/build_history', methods=['POST'])
def build_history():
    '''构建记录'''
    data = request.get_json()
    project_info = Project.query.filter_by(id=data.get('project_id', None), is_valid=True).first()
    if project_info is None:
        return bad_request('项目不存在')
    data['builded_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    builded_info = BuildHistory()
    builded_info.from_dict(data)
    db.session.add(builded_info)
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )
