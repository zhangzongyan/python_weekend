# -*- coding: utf-8 -*-
#   File Name：     04抽象接口类
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26

from abc import ABCMeta, abstractmethod


# 接口类
class TestMeta(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def delete(self):
        pass


class Student(TestMeta):
    def add(self):
        print("add....")
    def delete(self):
        print("delete.....")

test = Student()
test.add()
test.delete()

