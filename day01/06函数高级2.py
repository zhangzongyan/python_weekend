# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     06函数高级2
   Description :
   Author :       zongyanzhang
   date：          2018/8/12
-------------------------------------------------
   Change Activity:
                   2018/8/12:
-------------------------------------------------
"""
__author__ = 'admin'

# 列表生成式
l = [x for x in range(100) if x % 2 == 0]

l2 = []
for i in range(100):
    if i % 2 == 0:
        l2.append(i)
print(l)
print(l2)

from collections import Iterable, Iterator

# generator 生成器--->节省内存
l = (x for x in range(10) if x % 2 == 0)
print(type(l))
print(isinstance(l, Iterable))
for i in l:
    print(i, end=" ")
print()

a = 10
b = 20
a, b = (b, a)

# 函数----》生成器
def fib(n):
    a, b = 0, 1
    #l = []
    while n > 0:
        #l.append(b)
        yield b #pause
        a, b = b, a+b
        n -= 1
    #return l

f = fib(20)
print(type(f))

while True:
    try:
        print(next(f))
    except:
        break

# 可迭代(for)    迭代器(next)
print(isinstance(f, Iterator))

print(isinstance([], Iterable))
print(isinstance([], Iterator))

l = [1,2,3,54,6]
l2 = iter(l) # 将可迭代序列转换成迭代器
print(type(l2))

