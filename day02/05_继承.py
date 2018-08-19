# -*- coding: utf-8 -*-
#   File Name：     05_继承
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

# 飞机类
class Plane(object):
    def __init__(self, path, size, pos=(0,0)):
        self.imgpath = path
        self.size = size
        self.pos = pos

    def move(self):
        print("飞机动起来了")

class HeroPlane(Plane):
    '''继承'''
    def __init__(self, enegy):
        # 调用父类init
        Plane.__init__(self, "./heroplane", (50, 50))
        self.enegy = enegy

    # 重写父类方法
    def move(self):
        Plane.move(self)
        print("我是英雄")


hero = HeroPlane(100)
print(hero.imgpath, hero.size, hero.pos)
hero.move()


