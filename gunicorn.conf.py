workers = 5    # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
worker_class = "gevent"   # 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:5000"
debug = False
# 设置守护进程【关闭连接时，程序仍在运行】
daemon = True
# 设置超时时间120s，默认为30s。按自己的需求进行设置
timeout = 120
accesslog = '/home/www/logs/gunicorn_acess.log'
errorlog = '/home/www/logs/gunicorn_error.log'
# 设置日志记录水平
loglevel = 'warning'
preload_app = True
