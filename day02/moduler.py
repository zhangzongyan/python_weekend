# -*- coding: utf-8 -*-
#   File Name：     02_四则运算
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

def add2num(a, b):
    return a + b


def sub2num(a, b):
    return a - b

# __name__属性在本模块中值是__main__ 其他模块中值是模块名
if __name__ == "__main__":
    print(add2num(1, 2))
    print(sub2num(1, 2))

