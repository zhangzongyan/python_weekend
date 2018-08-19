# -*- coding: utf-8 -*-
#   File Name：     06_多态
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

class Animal:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, nm):
        self.__name = nm

    def bark(self):
        print("叫 叫 叫")


class Dog(Animal):
    # 重写
    def bark(self):
        print("旺 旺 旺")

class Cat(Animal):
    # 重写
    def bark(self):
        print("喵 喵 喵")

# 动物叫两声----->多态（同一个类型不同表现形式）
def bark_twice(animal):
    animal.bark()
    animal.bark()

if __name__ == '__main__':
    dog1 = Dog()
    dog1.name = "旺财"
    print(dog1.name)
    dog1.bark()

    cat1 = Cat()
    cat1.bark()

    print(isinstance(dog1, Animal))
    print(isinstance(cat1, Animal))

    # 调用bark_twice
    bark_twice(dog1)
    bark_twice(cat1)


