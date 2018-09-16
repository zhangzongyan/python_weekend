# -*- coding: utf-8 -*-
#   File Name：     05mysqllite
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/16

import sqlite3

# 创建连接
conn = sqlite3.connect("./test.db")

# 构建游标对象
cur = conn.cursor()

# 执行sql语句
cur.execute('''CREATE TABLE IF NOT EXISTS student(id integer PRIMARY KEY, \
name text NOT NULL, age integer)''')

try:
    # 插入一个数据
    cur.execute('''INSERT INTO student(id, name, age) VALUES (2, 'python2', 20)''')
except Exception as e:
    print("can not insert it:%s" % e)

res = cur.execute('''select * from student''')
for i in res:
    print(i)

# 提交
conn.commit()

# 关闭
conn.close()
