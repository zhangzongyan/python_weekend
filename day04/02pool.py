# -*- coding: utf-8 -*-
#   File Name：     02pool
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

from multiprocessing import Pool
import time

def job1(s):
    print("job1", s)
    time.sleep(3)

def job2(s):
    print("job2", s)

if __name__ == '__main__':
    # 实例化进程池对象
    p = Pool(3)

    # 向池中添加进程
    """
    # 异步
    p.apply_async(func=job1, args=("hello",))
    p.apply_async(func=job2, args=("world",))
    """
    # 同步
    p.apply(func=job1, args=("hello",))
    p.apply(func=job2, args=("world",))

    # 不再向池中添加新进程
    p.close()
    #time.sleep(3)
    # 终止池中所有的进程
    #p.terminate()
    # 为进程池所有的子进程收尸
    p.join()
    print("main.....")
