# -*- coding: utf-8 -*-
#   File Name：     07缓存区
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26

import time, sys

'''
缓存方式:
    行缓存:stdout stdin
    全缓存:文件
    无缓存:stderr
缓存区作用：
    合并系统调用（较少读写磁盘的次数）
'''

while True:
    print("hello world", end="") # 标准输出是行缓存
    # 强势刷新缓存区
    sys.stdout.flush()
    time.sleep(1)

