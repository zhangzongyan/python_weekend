# -*- coding: utf-8 -*-
#   File Name：     08ipc_pipe
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/9

from multiprocessing import Pipe, Process
from time import sleep

# 写管道
def write_pipe(conn):
    sleep(3)
    conn.send("hello!python")
    conn.send(100)
    conn.close()

# 读管道
def read_pipe(conn):
    data = conn.recv() # block
    print("read:", data)
    data = conn.recv()  # block
    print("read:", data)
    conn.close()

if __name__ == '__main__':
    # 管道
    (conn1, conn2) = Pipe(False)

    p1 = Process(target=write_pipe, args=(conn2, ))
    p2 = Process(target=read_pipe, args=(conn1, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("all done")
