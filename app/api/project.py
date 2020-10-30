# -*- coding: UTF-8 -*-
from datetime import datetime
from flask import request, jsonify
from app import db
from app.api.auth import token_auth
from app.api.errors import bad_request, error_response, not_found_error
from app.models.project import Project
from app.spider.get_api_docs import ApiDocsHelper
from . import bp

@bp.route('/project/list', methods=['GET'])
@token_auth.login_required
def project_list():
    """ 项目列表 """
    filterlist = []
    page = int(request.args.get('page'))
    per_page = int(request.args.get('limit'))
    project = request.args.get('project', '')
    env = request.args.get('env', '')
    filterlist.append(Project.is_valid==True)
    if project:
        filterlist.append(Project.project.like('%' + project + '%'))
    if env:
        filterlist.append(Project.env == env)
    data = Project.query.filter(*filterlist)
    if project is None and env is None:
        data = Project.query.filter_by(is_valid=True)
    data = Project.to_collection_dict(data, page, per_page, 'web.project_list')
    return jsonify(data)


@bp.route('/project/add', methods=['POST'])
@token_auth.login_required
def project_add():
    """ 项目添加 """
    data = request.get_json()
    if Project.query.filter_by(swagger_url=data.get('swagger_url', None), is_valid=True).first():
        return bad_request('项目Swagger地址已存在')
    data['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    project_data = Project()
    project_data.from_dict(data)
    db.session.add(project_data)
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )


@bp.route('/project/update', methods=['POST'])
@token_auth.login_required
def project_edit():
    """项目编辑"""
    project_data = request.get_json()
    project_id = project_data['id']
    project_info = Project.query.filter_by(id=project_id, is_valid=True).first()
    if project_info is None:
        return not_found_error(404)
    project_info.from_dict(project_data)
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )


@bp.route('/project/delete', methods=['DELETE'])
def project_del():
    """项目删除"""
    project_id = request.get_json()['id']
    pj = Project.query.filter_by(id=project_id, is_valid=True).first()
    if pj is None:
        return error_response(403)
    pj.is_valid = False
    db.session.add(pj)
    db.session.commit()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )


@bp.route('/project/get_api_docs', methods=['POST'])
def get_api_docs():
    """爬取Swagger"""
    project_data = request.get_json()
    project_id = project_data['id']
    pj_info = Project.query.filter_by(id=project_id).first_or_404()
    if pj_info is None:
        return not_found_error(404)
    swagger_url = pj_info.swagger_url
    project_id = pj_info.id
    docs_status = pj_info.docs_state
    ApiDocsHelper(swagger_url, project_id, docs_status).api_info()
    return jsonify(
        {
            "status": 200,
            "data": "success"
        }
        )


# @bp.route('/project/api_docs_list/<int:page>')
# def api_docs_list(page=1):
#     """接口信息列表 """
#
#     # 页码上限
#     page_size = 10
#     # 查询
#     path = request.args.get('path', '')
#     if path:
#         page_data = ApiDocs.query.filter(ApiDocs.path.contains(path)).paginate(page=page, per_page=page_size)
#     else:
#         page_data = ApiDocs.query.paginate(page=page, per_page=page_size)
#
#     return render_template('project/api_docs_detail.html', page_data=page_data)


# @bp.route('/product/detail/<project_id>')
# def project_detail(project_id):
#     """项目及接口详情"""
#     pj_detail = Project.query.filter_by(id=project_id).first_or_404()
#     return render_template('project/project_detail.html', pj_detail=pj_detail)
