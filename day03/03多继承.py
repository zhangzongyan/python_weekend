# -*- coding: utf-8 -*-
#   File Name：     03多继承
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26
#####################################

class A:
    def foo(self):
        print("foo A")

class B(A):
    def foo(self):
        super().foo()
        print("foo B")

class C(A):
    def foo(self):
        super().foo()
        print("foo C")

class D(B, C):
    def foo(self):
        super().foo()
        print("foo D")


print(C.__mro__)
c = C()
c.foo()

print(D.__mro__) # python3多继承是广度优先
d = D()
d.foo()
