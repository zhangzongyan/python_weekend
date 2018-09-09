# -*- coding: utf-8 -*-
#   File Name：     06myio
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26

"""
打开
    open()
读 / 写
    read() / write()
定位文件
    seek()
关闭
    close()
"""
"""
fp文件流
    open mode:
        方式
            "r":默认
            "r+"
            "w":
            "w+":
            "a":
            "a+":
            "x":
        模式
            "t":默认  str
            "b": 二进制 (图片...)
    
    encoding:
        编码方式    
    
"""
fp = open("text", mode='w+', encoding="utf-8")
#print(fp)


# 读
"""
read(size=-1)
    size为-1时表示读文件的全部
    不提倡读全部,占用内存过大
"""
"""
while True:
    #data = fp.read(5)
    data = fp.readline() # readlines()读取所有行
    if data == "": # 文件末尾
        break
    print(data, end="")
"""

# 写
fp.write("hello")
fp.writelines(["aa\n", "bb", "python"])

# 刷新文件缓存区
fp.flush()

# 获取文件偏移量
print(fp.tell())

# 设置文件偏移量
"""
seek(offset_size, position)
    position: 0 / SEEK_SET

fp.seek(0, 0)

print(fp.read())
"""
"""
文件描述符
    0   stdin
    1   stdout
    2   stderr
"""
print(fp.fileno())

fp.close()

# 避免文件忘记关闭

with open("text") as f:
    pass


