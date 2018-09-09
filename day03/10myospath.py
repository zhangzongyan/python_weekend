# -*- coding: utf-8 -*-
#   File Name：     10myospath
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26
import os.path as op


print(op.abspath("./text")) # 绝对路径

print(op.dirname(r"E:\python_weekend\day03\text")) # 目录名字

# 判断文件是否存在
if op.exists("abc"):
    print("存在")
else:
    print("不存在")

# 文件的字节个数
print(op.getsize("./text"))



