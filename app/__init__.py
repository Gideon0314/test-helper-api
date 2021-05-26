# -*- coding: UTF-8 -*-
from flask import Flask
from flask_cors import CORS
from app.models import db
from app.api import bp
from app.task import scheduler
from config import Config

__author__ = 'Gideon'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app=app)
    db.create_all(app=app)
    # Session(app)
    scheduler.init_app(app)
    from app.task import test_task
    scheduler.start()
    register_blueprint(app)
    CORS(app)
    return app


def register_blueprint(app):
    app.register_blueprint(bp, url_prefix='/api')
