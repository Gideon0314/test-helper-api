# -*- coding: UTF-8 -*-
import uuid
from . import db, PaginatedAPIMixin
from sqlalchemy.dialects.mysql import LONGTEXT

class Project(PaginatedAPIMixin, db.Model):
    """ 项目列表 """
    __tablename__ = 'project'

    id = db.Column(db.String(128), primary_key=True, default=uuid.uuid4, nullable=False, unique=True)
    # 项目名称
    project = db.Column(db.String(128), nullable=False)
    # 项目环境（开发/测试/预生产/生产）
    env = db.Column(db.String(128), nullable=False)
    # 项目版本
    version = db.Column(db.String(128))
    # 项目Swagger地址
    swagger_url = db.Column(db.NVARCHAR(500), nullable=False)
    # 获取Api状态
    docs_state = db.Column(db.Integer, default=0)
    # 接口更新信息
    update_info = db.Column(db.UnicodeText)
    # 逻辑删除
    is_valid = db.Column(db.Boolean, default=True)
    # 排序
    reorder = db.Column(db.Integer, default=0)
    # 创建时间
    created_at = db.Column(db.DateTime)
    # 最后修改的时间
    updated_at = db.Column(db.DateTime, index=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'project': self.project,
            'swagger_url': self.swagger_url,
            'version': self.version,
            'env': self.env,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else self.created_at,
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M:%S") if self.updated_at else self.updated_at,
            'status': self.docs_state
        }
        return data

    def from_dict(self, data):
        for field in ['project', 'env', 'swagger_url', 'created_at']:
            if field in data:
                setattr(self, field, data[field])
