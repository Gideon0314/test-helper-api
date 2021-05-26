# -*- coding: UTF-8 -*-
import sys
import os
from config import Config
sys.path.append(os.path.dirname(sys.path[0]))
from app import create_app


app = create_app(Config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)
    # Manager.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)
    #单进程、单线程
    # processes = 1
    # 10 个请求
