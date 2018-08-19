# -*- coding: utf-8 -*-
#   File Name：     03_面向对象
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

'''
类：抽象类型
对象：具体的， 一切皆对象
实例化：从类实例到对象的过程
属性：描述对象的特征
    实例属性
    类属性
方法：描述对象的行为（函数）
'''

# 类的定义
class Person:
    role = "人" # 类属性
    # 实例化对象自动调用的方法
    def __init__(self, name, age):
        self.name = name # 对象的属性（实例属性）
        self.age = age
    # 方法
    def eat(self):
        print("马上就吃饭")

if __name__ == '__main__':
    # 实例化对象
    p1 = Person("python", 20)

    # 实例属性的访问: 对象名.属性名
    print(p1.name, p1.age)
    # 类属性的访问: 对象名.属性名  / 类名.属性名
    print("role", p1.role)
    print("role", Person.role)

    p1.name = "mysql"
    print(p1.name, p1.age)

    # 调用对象的方法
    p1.eat()


