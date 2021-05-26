# -*- coding: UTF-8 -*-
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_cors import CORS
from app.api import bp
from app.extensions import scheduler
from app.models import db


__author__ = 'Gideon'


def create_app(config_class=None):
    try:
        app = Flask(__name__)
        configure_app(app, config_class)
        configure_extensions(app)
        configure_logging(app)
        register_blueprint(app)
        scheduler.init_app(app)
        from app.task import test_task
        scheduler.start()
        return app
    except Exception as e:
        raise e



def configure_app(app, config_class):
    app.config.from_object(config_class)
    # 不检查路由中最后是否有斜杠/
    app.url_map.strict_slashes = False


def register_blueprint(app):
    app.register_blueprint(bp, url_prefix='/api')


def configure_extensions(app):
    """Configures the extensions."""
    # Enable CORS
    CORS(app)
    # Init Flask-SQLAlchemy
    db.init_app(app=app)
    db.create_all(app=app)


def configure_logging(app):
    """Configure Logging."""
    logging.getLogger("apscheduler").setLevel(logging.INFO)
    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/tester.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Flask API Startup')
