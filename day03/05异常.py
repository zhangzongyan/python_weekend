# -*- coding: utf-8 -*-
#   File Name：     05异常
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26

# l = [1,2,3]

# print(l[5])

"""

try:
    print("hello world")

    # 抛出异常
    raise IndexError("这是一个测试异常....")
except IndexError as e:
    # 捕获异常
    print("Index Error 发生了:%s" % e)
"""


def div2num(x, y):
    assert y != 0 # 断言如果为False则抛出异常AssertionError
    return x // y

'''
BaseException 所有异常类的基类
Exception 常见异常类的基类
'''

print(div2num(10, 0))


"""
try:
    res = div2num(10, 0)
#except ZeroDivisionError as e:
except Exception as e:
    print("error: %s" % e)
else:
    print("the result is %d" % res)
finally:
    print("bye-bye")
"""
