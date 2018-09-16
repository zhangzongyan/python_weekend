# -*- coding: utf-8 -*-
#   File Name：     02udp
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/16
"""
    报式套接字:
        无连接，不可靠
        快

    服务端:
        socket()
        bind()
        recvfrom() / sendto()
        close()
"""
import socket

# 构建套接字
sd = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 绑定地址
sd.bind(("0.0.0.0", 9999))

while True:
    data, raddr = sd.recvfrom(1024) # 1K

    print("From ip:{}, port:{}".format(*raddr))
    print(data.decode())

sd.close()
