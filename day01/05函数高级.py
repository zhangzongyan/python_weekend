# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05函数高级
   Description :
   Author :       zongyanzhang
   date：          2018/8/12
-------------------------------------------------
   Change Activity:
                   2018/8/12:
-------------------------------------------------
"""
__author__ = 'admin'

from functools import reduce

# 函数是可以作为参数
def twice(f):
    f()
    f()

def fun():
    print("happy everyone")

f = fun
print(type(f))
f()

twice(fun)

# 高阶函数:函数作为参数
def change(s):
    if len(s) > 1:
        return None
    # s只有一个字符

    if s.isupper():
        return s.lower()
    else:
        return s.upper()

def mi(n):
    return n*n

l = ['a', 'M', 'p', 'n']
res = map(change, l)
print(list(res))
print(type(res))

l = [1,2,3,4,5,6,7]

l2 = list(map(str, l))
print(l2)

l3 = list(map(mi, l))
print(l3)

# reduce
def test1(m, n):
    return m+n
res = reduce(test1, [1,2,3,4,5])
print(res)


# sorted
l4 = ["ZEllo", "world", "Python", "python"]
print(sorted(l4, key=str.lower, reverse=True))

