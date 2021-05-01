# -*- coding: UTF-8 -*-
import uuid
from . import db


class BuildHistory(db.Model):
    """Api信息"""
    __tablename__ = 'build_history'

    id = db.Column(db.String(128), primary_key=True, default=uuid.uuid4, nullable=False, unique=True)
    # 关联的项目id
    project_id = db.Column(db.String(128), db.ForeignKey('project.id'))
    # 构建分支
    git_branch = db.Column(db.String(128))
    # 创建时间
    builded_at = db.Column(db.DateTime)

    def to_dict(self):
        data = {
            'id': self.id,
            'project_id': self.project_id,
            'git_branch': self.git_branch,
            'builded_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.builded_at else self.builded_at,
        }
        return data

    def from_dict(self, data):
        for field in ['project_id', 'git_branch', 'builded_at']:
            if field in data:
                setattr(self, field, data[field])
