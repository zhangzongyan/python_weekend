# -*- coding: utf-8 -*-
#   File Name：     11os
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26
import os

print(os.name)

print(os.environ)

# 文件属性信息
print(os.stat("./text"))

# shutil.rmtree()删除文件
