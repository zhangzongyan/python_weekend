# -*- coding: utf-8 -*-
#   File Name：     02元类
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26


class Test(object):
    def hello(self):
        print("good morning")


t = Test()
t.hello()

# 通过type创建类

def sayHello(self):
    print("hello...")


# type(类名， 继承基类元祖, 字典(类的属性和行为))
Student = type("student_class", (object,), {"hello":sayHello, "name":"guido"})

stu = Student()
print(stu.name)
stu.hello()
print(Student.__name__)


"""
指定构建类的行为:类模板----->元类
"""

def listadd(self, elm):
    self.append(elm)


class ListMetaclass(type):
    def __new__(cls, name, bases, attr):
        attr['add'] = listadd
        return type.__new__(cls, name, bases, attr)


# 构建列表类
class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add(100)
print(l)
