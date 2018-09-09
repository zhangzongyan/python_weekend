# -*- coding: utf-8 -*-
#   File Name：     09thread
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

from threading import Thread
import time

"""
python多线程 设置GIL全局锁
    因为GIL存在，多线程不能并行
"""

count = 1000 # 多线程 共享的count

# 线程函数
def thr_job():
    print("hello everyone")
    global count
    if count >= 1000:
        print("get it")
        count -= 1000


if __name__ == '__main__':
    t = []

    for i in range(4):
    # 创建线程对象
        t.append(Thread(target=thr_job))

    # 使能线程
    for i in t:
        i.start()
    # 线程收尸
    for i in t:
        i.join()
        print(i.name)

