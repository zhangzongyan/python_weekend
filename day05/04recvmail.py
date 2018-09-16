# -*- coding: utf-8 -*-
#   File Name：     04recvmail
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/16

import poplib

# 连接pop服务器
server = poplib.POP3("pop.163.com")

# 欢迎信息
print(server.getwelcome().decode())

# 用户密码
server.user("python_1989@163.com")
server.pass_("python999")

# 获取邮件总数目和大小
print(server.stat())

# 获取所有邮件信息(索引，大小)
req, msglist, oct = server.list()
print(msglist)
# print(req, oct)

# 最后一封邮件
req, msg, oct = server.retr(len(msglist))
print(msg)

res = b'\r\n'.join(msg)
lastmail = res.decode()
print(lastmail)

server.quit()

