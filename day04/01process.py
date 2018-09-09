# -*- coding: utf-8 -*-
#   File Name：     01process
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

import multiprocessing
import time


# 进程函数
def fun(s):
    print("hello", s)
    time.sleep(1)

if __name__ == '__main__':
    # 实例化进程对象
    pro_obj = multiprocessing.Process(target=fun, args=("python",))

    # 使能进程
    pro_obj.start()

    # 收尸, 等待进程对象pro_obj终止
    pro_obj.join()

    print("bye-bye")


