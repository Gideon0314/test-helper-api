# -*- coding: UTF-8 -*-
import uuid
from . import db, PaginatedAPIMixin


class TaskBoard(PaginatedAPIMixin, db.Model):
    """ 测试任务表 """
    __tablename__ = 'task_board'

    id = db.Column(db.String(128), primary_key=True, default=uuid.uuid4, nullable=False, unique=True)
    # 关联的主任务id
    task_id = db.Column(db.String(128), db.ForeignKey('task.id'))
    # 主域名
    domain = db.Column(db.Column(db.NVARCHAR(500), nullable=False))
    # 任务名称
    subtask_name = db.Column(db.String(128), nullable=False)
    # 描述
    remark = db.Column(db.String(256), nullable=False)
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
            'task_name': self.task_name,
            'env': self.env,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else self.created_at,
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M:%S") if self.updated_at else self.updated_at,
            'remark': self.remark
        }
        return data

    def from_dict(self, data):
        for field in ['task_name', 'env', 'remark']:
            if field in data:
                setattr(self, field, data[field])
