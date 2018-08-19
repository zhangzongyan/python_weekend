# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     04函数
   Description :
   Author :       zongyanzhang
   date：          2018/8/12
-------------------------------------------------
   Change Activity:
                   2018/8/12:
-------------------------------------------------
"""
__author__ = 'admin'

glob = 100

# 使用默认参数列表时注意，多次调用时同一个列表
def test(n, l=[]):
    global glob # 在函数内使用的就是全局glob
    glob = 200

    l.append(n)
    return l

print(test(10))
print("main:", glob)

print(test(5, l=[1,2,3]))

print(test(3))

