# -*- coding: utf-8 -*-
#   File Name：     01_装饰器
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

import time
import functools


# 实现装饰器
def deractor(fun):
    @functools.wraps(fun) # 将fun的属性赋值给wrpper
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        # 装饰语句
        print("hello world")
        return fun(*args, **kwargs)

    return wrapper


@deractor
def now(m, n):
    '''这是一个要被装饰函数的函数'''
    print(time.ctime(), m, n)

if __name__ == '__main__':
    now(1, n=2) # now = derector(now)
    print(now.__doc__)
    print(now.__name__)

