# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03函数
   Description :
   Author :       zongyanzhang
   date：          2018/8/12
-------------------------------------------------
   Change Activity:
                   2018/8/12:
-------------------------------------------------
"""
__author__ = 'admin'


# 函数的定义---->位置参数
def sum2num(num1, num2): # num1 num2形参
    res = num1 + num2
    return res

# 函数功能：求得一个整型数的n次方--->默认参数
def mi(num, n=2):
    res = 1
    while n > 0:
        res *= num
        n -= 1
    return res

# 求所有参数和的n次方---->*arg可变参数 可变参数在默认参数前面
def sumn(*arg, n=2):
    #print(type(arg))
    s = 0
    for a in arg:
        s += a
    return mi(s, n)


# 关键字参数
def studentInfo(**kwargs):
    print(type(kwargs), kwargs)


if __name__ == '__main__':
    # 函数的调用
    a = 10
    b = 20
    r = sum2num(a, b) # 实参
    print("{} + {} = {}".format(a, b, r))

    print(mi(10,3))
    print(mi(5, 4))

    print(sumn(1,2,3,n=3))

    print(studentInfo(name="python", age=29))

    #print("hello", "world", "girl", "boy", sep="\n", end="")


