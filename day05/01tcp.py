# -*- coding: utf-8 -*-
#   File Name：     01tcp
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/16
#########################################

"""
TCP：
    创建连接的，可靠的传输
服务端(被动,先运行)         客户端（主动的）
socket()                  socket()
bind()                    bind()可省略
listen()
accept()                  connect()
recv() / send()           recv() / send()
close()                   close()

"""
# Server
import socket
from multiprocessing import Pool

# 工作进程函数
def job(conn_sd):
    conn_sd.send(b'ok')
    conn_sd.close()

def main():
    # 流式套接字对象
    sd = socket.socket()

    try:
        # 为套接字绑定地址
        sd.bind(("0.0.0.0", 6667))
    except Exception as e:
        print(e)
        return None
    # 处于监听状态
    sd.listen(20)

    # 实例化进程池
    pool = Pool()

    while True:
        # 接受连接 newsd数据交换的 raddr对端地址
        try:
            newsd, raddr = sd.accept()
            print("request from ip:{}, port:{}".format(raddr[0], raddr[1]))
            # 向池中添加新进程
            pool.apply_async(func=job, args=(newsd,))

        except:
            sd.close()
            pool.terminate()
            break

if __name__ == '__main__':
    main() # 多进程在控制语句main中


