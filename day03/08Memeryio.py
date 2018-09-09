# -*- coding: utf-8 -*-
#   File Name：     08Memeryio
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/26

import io

# io发生在内存

# StrinIO类型的对象，在内存中进行读写操作，数据类型必须是str
memyio = io.StringIO()
memyio.write("hello")
#memyio.write(b"afternoon") 只能写str类型的数据

print(memyio.getvalue())

# ByteIO同样是在内存中读写，数据类型必须是bytes
memyio2 = io.BytesIO(b"hello")
print(memyio2.getvalue())

memyio2.write(b'python')
print(memyio2.getvalue())
print(memyio2)


