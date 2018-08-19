# -*- coding: utf-8 -*-
#   File Name：     07_课堂练习
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

'''
定义字典类:
    1.删除某个key
        del_dict(key)
    2.判断某个key是否在字典对象中，如果在返回value，否则返回"not found"
    3.返回键组成的列表
    4.合并字典
'''

class MyDict:
    def __init__(self, **kwargs):
        self.dt = kwargs

    # 显示字典
    def showdict(self):
        print(self.dt)

    # 删除
    def del_dict(self, key):
        self.dt.pop(key)

    def has_key(self, key):
        return key in self.dt

    def all_keys(self):
        return list(self.dt.keys())

    def merge_dict(self, newdt):
        self.dt.update(newdt)


# 创建一个字典
d1 = MyDict(a = 1, b = 2, c = 3)
d1.showdict()

d1.del_dict("a")
d1.showdict()

print(d1.has_key("b"))

print(d1.all_keys())

d1.merge_dict(dict(aa = 2, bb = 3, cc = 4))
d1.showdict()
