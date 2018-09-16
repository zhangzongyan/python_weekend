# -*- coding: utf-8 -*-
#   File Name：     01client
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/16
#####################################

"""
客户端
"""

import socket

# 1
sd = socket.socket()

sd.connect(("172.25.3.153", 6667))

recv_data = sd.recv(100)
print(recv_data.decode())

sd.close()
