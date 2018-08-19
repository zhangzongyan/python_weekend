# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       zongyanzhang
   date：          2018/8/12
-------------------------------------------------
   Change Activity:
                   2018/8/12:
-------------------------------------------------
"""
__author__ = 'admin'

import time
import sys, random

l = ["你","好", "吗"]

while True:
    print("\r",l[random.randint(0,3)], end="")
    sys.stdout.flush() #刷新输出缓存区
    time.sleep(1)
