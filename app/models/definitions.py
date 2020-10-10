# -*- coding: UTF-8 -*-
import uuid
from . import db


class Definitions(db.Model):
    """Api信息"""
    __tablename__ = 'definitions'

    id = db.Column(db.String(128), primary_key=True, default=uuid.uuid4, nullable=False, unique=True)
    # 关联的项目id
    project_id = db.Column(db.String(128), db.ForeignKey('project.id'))
    # 接口描述
    title = db.Column(db.String(128), nullable=False)
    # 关联的项目id
    properties = db.Column(db.Text)
    #
    type = db.Column(db.String(128), nullable=False)
