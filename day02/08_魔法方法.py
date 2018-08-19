# -*- coding: utf-8 -*-
#   File Name：     08_魔法方法
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

# 魔法方法 魔法属性
'''
    __init__:实例化对象时自动调用---》构造方法
    __del__: 对象销毁时自动调用的--->析构
    __str__: 打印对象的时候自动调用
    __iter__ 和__next__:
        __iter__循环遍历对象时首先调用此方法
        __next__每循环一次就会调用一次__next__方法，知道接收到StopIteration异常为止
    __len__:
        len()自动调用的
'''
class Color(object):
    '''测试类'''
    __slots__ = ("value",) # 实例属性只能有元祖中所包含的属性

    def __init__(self):
        print("构建对象")
        #self.age = 100

    def __del__(self):
        print("对象销毁")

    def __str__(self):
        return "in file {}, create a new object" .format( __file__)

    def __iter__(self):
        print("__iter__ is called")
        self.value = 5
        return self
    def __next__(self):
        print("__next__ is called")
        self.value -= 1
        if self.value <= 0:
            raise StopIteration
        return self.value

    def __len__(self):
        return 100


# dir(class)获取此类所有的属性和方法
print(dir(list))
print(dir(Color))
print(Color.__dict__)

c = Color()

print("hello world")

print(c)

# 遍历对象
for i in c:
    print(i)

# 对象的长度
print(len(c))

# 为实例添加新的属性
c.name = "魔法"
print(c.name)


