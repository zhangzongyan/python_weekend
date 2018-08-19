# -*- coding: utf-8 -*-
#   File Name：     04_面向对象
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

class Student(object):
    '''这是测试学生类'''
    def __init__(self, name): # 构造方法
        self.__name = name# 私有属性

    def getName(self):
        print(self.__name)

    def setName(self, nm):
        if nm == "" or len(nm) > 6:
            return None
        self.__name = nm

    @property # 访问器
    def abc_age(self):
        return self.__age
    # 设置age属性
    @abc_age.setter # 设置器
    def age(self, age):
        print("立即设置age属性")
        if age > 0:
            self.__age = age
    # 获取年龄
    @property
    def birth(self):
        return 2018-self.__age


if __name__ == '__main__':
    stu1 = Student("hello")

    stu1.setName("aaaaaaaaaa")
    stu1.getName()

    #stu1.setage(10)
    stu1.age = 10 #stu1.age(10)
    print(stu1.abc_age)
    print(stu1.birth)

    #print(stu1._Student__name) # 不推荐

    print(stu1.__dict__)
    print(stu1.__doc__)

