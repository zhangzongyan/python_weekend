# -*- coding: utf-8 -*-
#   File Name：     05ipc
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

from multiprocessing import Process,Value

num = 10


def job(arg):
    global num
    num = 100
    arg.value = 1000 # arg对象


if __name__ == '__main__':
    """
        多进程间共享内存
            multiprocessing.Value()
            multiprocessing.Array()
    """
    # shared memory
    val = Value('i', 100)

    p = Process(target=job, args=(val,))
    p.start()
    p.join()
    print(num, val.value)

