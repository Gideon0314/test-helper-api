# -*- coding: UTF-8 -*-
from pprint import pprint
from flask import request, redirect, url_for, abort, jsonify
# from app.froms.project import ProjectForm
# from app.models.project import Project
# from app.models.api_docs import ApiDocs
# from app.models import db
# from app.spider.get_api_docs import ApiDocsHelper
from app.models.project import Project
from . import bp

def project_list_json(data):
    list = []
    for item in data:
        list.append(
            {
                'version': item.version,
                'env': item.env,
                'name': item.name,
                'id': item.id,
                'swagger_url': item.swagger_url,
            }
        )
    return list

@bp.route('/project/list', methods=['GET'])
def project_list():
    """ 项目列表 """
    # 页码
    page = int(request.args.get('page'))
    # 页码上限
    page_size = int(request.args.get('limit'))
    # 查询
    name = request.args.get('name', '')
    if name:
        page_data = Project.query.filter_by(name=Project.name.contains(name), is_valid=True).paginate(page=page, per_page=page_size)
    else:
        page_data = Project.query.filter_by(is_valid=True).paginate(page=page, per_page=page_size)
    return jsonify(project_list_json(page_data.items))


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
#
#
# @bp.route('/project/add', methods=['GET', 'POST'])
# def project_add():
#     """ 项目添加 """
#     form = ProjectForm()
#
#     if request.method == 'POST' and form.validate_on_submit():
#
#         # 保存到数据库
#         project_data = Project(
#             name=form.data['name'],
#             swagger_url=form.data['swagger_url'],
#             env=form.data['env']
#         )
#         db.session.add(project_data)
#         db.session.commit()
#         flash('新增项目成功', 'success')
#         return redirect(url_for('bp.project_list', page=1))
#
#     print(form.errors)
#     # else:
#     #     flash('项目信息填写有误', 'warning')
#     return render_template('project/project_add.html', form=form)
#
#
# @bp.route('/product/detail/<project_id>')
# def project_detail(project_id):
#     """项目及接口详情"""
#     pj_detail = Project.query.filter_by(id=project_id).first_or_404()
#     return render_template('project/project_detail.html', pj_detail=pj_detail)
#
#
# @bp.route('/project/edit/<project_id>', methods=['GET', 'POST'])
# def project_edit(project_id):
#     """项目信息编辑"""
#     pj_edit_info = Project.query.filter_by(id=project_id, is_valid=True).first()
#
#     if pj_edit_info is None:
#         abort(404)
#     form = ProjectForm(pj_edit_info=pj_edit_info)
#
#     if form.validate_on_submit():
#         pj_edit_info.name = form.name.data
#         pj_edit_info.swagger_url = form.data['swagger_url']
#         pj_edit_info.env = form.data['env']
#         db.session.add(pj_edit_info)
#         db.session.commit()
#         flash('修改成功')
#         return redirect(url_for('bp.project_list', page=1))
#     else:
#         print(form.errors)
#     return render_template('project/project_edit.html', form=form, pj_edit_info=pj_edit_info)
#
#
# @bp.route('/project/del/<project_id>', methods=['GET', 'POST'])
# def project_del(project_id):
#     """项目删除"""
#     pj = Project.query.filter_by(id=project_id, is_valid=True).first()
#     if pj is None:
#         return 'no'
#     pj.is_valid = False
#     db.session.add(pj)
#     db.session.commit()
#     return 'ok'
#
#
# @bp.route('/project/get_api_docs/<project_id>', methods=['GET', 'POST'])
# def get_api_docs(project_id):
#     """爬取Swagger"""
#     pj_info = Project.query.filter_by(id=project_id).first_or_404()
#     if pj_info is None:
#         abort(404)
#     swagger_url = pj_info.swagger_url
#     project_id = pj_info.id
#     ApiDocsHelper(swagger_url, project_id).api_info()
#     # flash('', 'success')
#     return redirect(url_for('bp.project_list', page=1))


def test_case():
    """执行当前测试计划"""
    pass

