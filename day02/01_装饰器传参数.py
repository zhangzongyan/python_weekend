# -*- coding: utf-8 -*-
#   File Name：     01_装饰器传参数
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

import functools

def log(text):
    def deractor(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            print(text)
            return fun(*args, **kwargs)
        return wrapper
    return deractor


@log('logloglog')
def now():
    print("hello world")

if __name__ == '__main__':
    now() #now = log('logloglog')()


