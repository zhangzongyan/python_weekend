# -*- coding: utf-8 -*-
#   File Name：     04pool
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

from multiprocessing import Pool
from time import sleep

def job(arg):
    print("start", arg)
    sleep(3)
    print("end", arg)
    return arg+1


if __name__ == '__main__':
    p = Pool(5)
    res = []

    for i in range(10):
        res.append(p.apply_async(func=job, args=(i, )))

    p.close()
    p.join()

    print("all processes exit-code:")
    for i in res:
        print(i.get(), end=" ")
    print()
