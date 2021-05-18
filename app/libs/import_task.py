# -*- coding: UTF-8 -*-
from functools import wraps

def task(func):
    @wraps(func)  #使用本条命令可以让func函数返回其本身的函数名等。
    def import_task(*args,**kwargs):
            print(func.__name__)
            print(func.__doc__)
            print('定时任务去重新增')
            ret = func(*args,**kwargs)
            return ret
    return import_task


@task
def func(*args, **kwargs):
    '''定时任务1'''
    print('this is a test')
    return()

if __name__ == '__main__':

    func('ok')
