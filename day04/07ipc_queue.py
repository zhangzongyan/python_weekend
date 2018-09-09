# -*- coding: utf-8 -*-
#   File Name：     06ipc_queue
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

from multiprocessing import Process, Queue
from time import sleep


def job1_write(q):
    l = [1, 2, 3, "hello"]
    for i in l:
        q.put(i) # 写队列
        sleep(1)


def job2_read(q):
    while True:
        try:
            res = q.get(timeout=5) # 读队列
            print(res)
        except:
            print("timeout now")
            break

if __name__ == '__main__':
    # 创建队列
    que = Queue(1024)

    p1 = Process(target=job1_write, args=(que, ))
    p2 = Process(target=job2_read, args=(que, ))

    p1.start()
    sleep(1)
    p2.start()

    p1.join()
    p2.join()
    print("all jobs done")

