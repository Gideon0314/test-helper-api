# -*- coding: UTF-8 -*-
from datetime import datetime
from flask import request, jsonify
from app import db
from app.api.errors import bad_request, error_response, not_found_error
from app.models.task import Task
from . import bp


@bp.route('/task/list', methods=['GET'])
def task_list():
    """ 任务列表 """
    filterlist = []
    page = int(request.args.get('page'))
    per_page = int(request.args.get('limit'))
    task_name = request.args.get('task_name', '')
    env = request.args.get('env', '')
    filterlist.append(Task.is_valid==True)
    if task_name:
        filterlist.append(Task.task_name.like('%' + task_name + '%'))
    if env:
        filterlist.append(Task.env == env)
    data = Task.query.filter(*filterlist)
    if task_name is None and env is None:
        data = Task.query.filter_by(is_valid=True)
    data = Task.to_collection_dict(data, page, per_page, 'web.task_list')
    return jsonify(data)

@bp.route('/task/add', methods=['POST'])
def task_add():
    """ 任务添加 """
    data = request.get_json()
    if Task.query.filter_by(task_name=data.get('task_name', None), is_valid=True).first():
        return bad_request('任务已存在')
    data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_data = Task()
    task_data.from_dict(data)
    db.session.add(task_data)
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )

@bp.route('/task/update', methods=['POST'])
def task_edit():
    """任务编辑"""
    task_data = request.get_json()
    task_id = task_data['id']
    task_info = Task.query.filter_by(id=task_id, is_valid=True).first()
    if task_info is None:
        return not_found_error(404)
    task_info.from_dict(task_data)
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )

@bp.route('/task/delete', methods=['DELETE'])
def task_del():
    """任务删除"""
    task_id = request.get_json()['id']
    task = Task.query.filter_by(id=task_id, is_valid=True).first()
    if task is None:
        return error_response(403)
    task.is_valid = False
    db.session.add(task)
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )

@bp.route('/task', methods=['GET'])
def task_board():
    """任务看板"""
    id = request.args.get('id')
    # task_id = request.get_json()['id']
    print(id)
    task = Task.query.filter_by(id=id, is_valid=True).first()
    # if task is None:
    #     return error_response(403)
    # task.is_valid = False
    # db.session.add(task)
    # db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )
