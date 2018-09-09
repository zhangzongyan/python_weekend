# -*- coding: utf-8 -*-
#   File Name：     03pool
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

from multiprocessing import Pool
import time


def job(i):
    print(i)
    time.sleep(3)


if __name__ == '__main__':
    p = Pool(8) # 默认进程池的大小是cpu个数  4

    p.map(job, "python") # 内置的map()
    p.close()
    p.join()

    print("main end...")
