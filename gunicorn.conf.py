# 定义同时开启的处理请求的进程数量，根据网站流量适当调整
workers = 1
# 采用gevent库，支持异步处理请求，提高吞吐量
worker_class = "gevent"
# 监听内网5000端口
bind = "0.0.0.0:5000"
# debug = False
# 设置守护进程【关闭连接时，程序仍在运行】
# daemon = True
# 设置超时时间120s，默认为30s。按自己的需求进行设置
# timeout = 120
# # 设置日志记录水平
loglevel = 'info'
# 设置访问日志
accesslog = '/usr/src/app/log/gunicorn_acess.log'
#错误信息日志
errorlog = '/usr/src/app/log/gunicorn_error.log'
#设置这个值为true 才会把打印信息记录到错误日志里
capture_output = True
# preload_app = True
