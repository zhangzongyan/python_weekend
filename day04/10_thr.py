# -*- coding: utf-8 -*-
#   File Name：     10_thr
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

"""
    在当前目录下，有一个"test.txt"文件,文件中有个0
    创建20个线程，同时读文件，并将文件现有的数值+1，覆盖写回文件
    问最后文件中的存放的数值是多少
"""
from threading import Thread, Lock

# 设置一个把全局的锁
lock = Lock()


# 线程函数
def thr_job():
    try:
        fp = open("./test.txt", "r+")
    except:
        return -1
    # 多线程发生竞争的这段代码称临界区，保证临界区安全使用互斥量(lock)
    lock.acquire() # 加锁
    data = fp.read()
    write_data = str(int(data) + 1)
    fp.seek(0, 0)
    fp.write(write_data)
    fp.close()
    lock.release() # 释放锁

    return 0


if __name__ == '__main__':

    thrs = []

    for i in range(20):
        t = Thread(target=thr_job)
        thrs.append(t)
        t.start()
    for i in thrs:
        i.join()

    print("all done")
