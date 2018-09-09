# -*- coding: utf-8 -*-
#   File Name：     oop_魔法
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26


class Person(object):
    """
    def __new__(cls, *args, **kwargs):
        print("new 调用了")
    """

    def __init__(self, name, age=1):
        self._name = name
        self._age = age

    @property
    def name(self): # 实例方法
        return self._name

    @name.setter
    def name(self, nm):
        print("self:%s" % self)
        self._name = nm

    # 类方法
    @classmethod
    def class_method(cls):
        print("这是一个类方法, cls:%s" % cls)

    # 静态方法
    @staticmethod
    def static_method():
        print("这是一个静态方法，就是一个在类内部定义的普通函数")


p1 = Person("Guidon", 50)
print(p1.name)

p1.name = "python"
print(p1.name)

Person.class_method() # 类方法的调用
p1.class_method()

Person.static_method()
p1.static_method()

