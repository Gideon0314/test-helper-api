# -*- coding: UTF-8 -*-
import uuid
from . import db


class ApiDocs(db.Model):
    """Api信息"""
    __tablename__ = 'api_docs'

    id = db.Column(db.String(128), primary_key=True, default=uuid.uuid4, nullable=False, unique=True)
    # 关联的项目id
    project_id = db.Column(db.String(128), db.ForeignKey('project.id'))
    # 接口描述
    api_summary = db.Column(db.String(128), nullable=False)
    # 标签
    tags = db.Column(db.String(128), nullable=False)
    # 接口path
    path = db.Column(db.NVARCHAR(500), nullable=False)
    # 请求类型
    request_method = db.Column(db.String(128), nullable=False)
    # 请求参数
    requests_definitions = db.Column(db.Text)
    # 返回参数
    responses_definitions = db.Column(db.Text)
    # 逻辑删除
    is_valid = db.Column(db.Boolean, default=True)
    # 排序
    reorder = db.Column(db.Integer, default=0)
    # 创建时间
    created_at = db.Column(db.DateTime)
    # 最后修改的时间
    updated_at = db.Column(db.DateTime)
