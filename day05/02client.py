# -*- coding: utf-8 -*-
#   File Name：     02client
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/16
####################################

"""
报式套接字客户端：
    socket()
    sendto()
    close()
"""
import socket

sd = socket.socket(type=socket.SOCK_DGRAM)

sd.sendto(b'i am ok', ("127.0.0.1", 9999))

sd.close()
