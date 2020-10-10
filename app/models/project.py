# -*- coding: UTF-8 -*-
import uuid
from . import db


class Project(db.Model):
    """ 项目列表 """
    __tablename__ = 'project'

    id = db.Column(db.String(128), primary_key=True, default=uuid.uuid4, nullable=False, unique=True)
    # 项目名称
    name = db.Column(db.String(128), nullable=False)
    # 项目环境（开发/测试/预生产/生产）
    env = db.Column(db.String(128), nullable=False)
    # 项目版本
    version = db.Column(db.String(128))
    # 项目Swagger地址
    swagger_url = db.Column(db.NVARCHAR(500), nullable=False)
    # 获取Api状态
    docs_state = db.Column(db.Integer, default=0)
    # 逻辑删除
    is_valid = db.Column(db.Boolean, default=True)
    # 排序
    reorder = db.Column(db.Integer, default=0)
    # 创建时间
    created_at = db.Column(db.DateTime)
    # 最后修改的时间
    updated_at = db.Column(db.DateTime, index=True)
