# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from app.models import db
from app.api import bp
from app.task import scheduler


__author__ = 'Gideon'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    # Session(app)
    app.config.from_object('app.setting')
    register_blueprint(app)
    CORS(app)
    db.init_app(app)
    db.create_all(app=app)
    # scheduler.init_app(app)
    scheduler.start()
    return app


def register_blueprint(app):
    app.register_blueprint(bp, url_prefix='/api')
