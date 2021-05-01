# -*- coding: UTF-8 -*-
import os
import base64
from datetime import datetime, timedelta
import jwt
from flask import url_for, current_app
from . import db, PaginatedAPIMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(PaginatedAPIMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))  # 不保存原始密码

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_dict(self, include_email=False):
        data = {
            "status": 200,
            "data":
                {
                'id': self.id,
                'name': self.username,
                'roles': [1],
                'avatar': "https://s3.ax1x.com/2021/01/10/s13xeO.jpg",
                '_links': {
                    'self': url_for('web.get_user')
                }
                }
        }
        if include_email:
            data['email'] = self.email
        return data

    def get_jwt(self, expires_in=6000):
        now = datetime.utcnow()
        payload = {
            'id': self.id,
            'name': self.username,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256')

    @staticmethod
    def verify_jwt(token):
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidSignatureError) as e:
            # Token过期，或被人修改，那么签名验证也会失败
            return None
        if User.query.get(payload.get('id')):
            return payload
        # return User.query.get(payload.get('id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])
