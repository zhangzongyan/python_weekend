# -*- coding: utf-8 -*-
#   File Name：     09序列化
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26

import pickle
"""
将对象转换成可以存储或者网络发送的数据格式的过程称为序列化
反之称为反序列化
"""

with open("text", "wb+") as f:
    d = dict(name='python', age=20)
    obj = pickle.dump(d, f) # 将字典对象序列化为可以直接写入文件的数据类型
    #f.write(obj)

    # 读出来在反序列化
    f.seek(0, 0)
    data = pickle.load(f)
    print(type(data), data)


# json通用数据格式
import json

l = [1, "hello", {'name':'python'}]
jl = json.dumps(l) # 序列化为json个数的数据
print(type(jl), jl)

l = json.loads(jl) # 反序列化为python数据格式
print(type(l), l)

with open("text", "w+") as f:
    d = dict(name='sunday', id=7)
    json.dump(d, f)
    f.seek(0, 0)
    k = json.load(f)
    print(type(k), k)


class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

"""
Student自定义类，json不支持
提供函数，返回json能够序列化的数据类型
"""
def parseStudent(stu):
    return {
        'name':stu._name,
        'age':stu._age
    }

s = Student("小白", 20)
print(s.__dict__)
#json.dumps(s, default=parseStudent)
jsonobj = json.dumps(s, default=lambda obj:obj.__dict__)
print(type(jsonobj))

s = json.loads(jsonobj)
print(type(s), s)


# 扩展实例
def test(n, *, hello="hello"):
    print(n, hello)


test(100, hello="world")
