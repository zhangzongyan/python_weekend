# -*- coding: utf-8 -*-
#   File Name：     06ipc_queue
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

"""
进程池中使用队列
"""

from multiprocessing import Pool, Manager
from time import sleep


def job1_write(q):
    l = [1, 2, 3, "hello"]
    for i in l:
        q.put(i)


def job2_read(q):
    while not q.empty():
        res = q.get()
        print(res)


if __name__ == '__main__':
    p = Pool(4)

    #################创建队列
    que = Manager().Queue(1024)

    p.apply_async(func=job1_write, args=(que, ))
    p.apply_async(func=job2_read, args=(que, ))

    print(p)

    p.close()
    p.join()
    print("all jobs done")

