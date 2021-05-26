# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import Flask
from app.models import db
from config import Config
from app.models import api_docs, definitions, project, user, task


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
