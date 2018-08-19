# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02序列类型
   Description :
   Author :       zongyanzhang
   date：          2018/8/12
-------------------------------------------------
   Change Activity:
                   2018/8/12:
-------------------------------------------------
"""
__author__ = 'admin'

'''(字符串 元祖)不可变 （列表）可变'''
def strTest():
    s = "python"
    '''
    print("py" in s)
    print("p" not in s)

    t = "最好的语言"
    s = s + t
    print(s)

    s = s * 10
    print(s)

    s = "apypthon"
    # 重要 可迭代
    for i in s:
        print(i)
    for i in range(len(s)):
        print(s[i]) # 可索引
    # 切片(正向递增0--->   反向递减-1) s[start:end:step=1]
    print(s[:3])
    print(s[3:])
    print("s[-1:-4]:", s[-1:-4:-1])
    print("逆序:", s[::-1])

    print("长度:", len(s))
    print("最大:", max(s))
    print("最小:", min(s))

    print("h的索引",s.index("h"))
    print("p出现%d次" % s.count("p"))

    res = ""
    for i in range(0,100,2):
        res = res+str(i)
    print(res)
    '''

    # 将指定字符串加入有序序列
    l = ["hello", "everyone"]
    newl = ",".join(l)
    print(newl)
    print(" ".join("hello"))

    # 切割字符串
    for i in "hello world python     after".split(" "):
        if i: # 去除空串
            print(i)

def listTest():
    l = [1, 2, 3, "hello"]
    l2 = [11,22,33,13]

    l = l + l2
    print(l)

    print("逆序:", l[::-1])
    print(max(l2))

    print(list("hello"))
    print(list(range(10)))

    # 排序
    print(sorted(l2))
    print("l2:",l2)
    l2.sort(reverse=True) # 列表本身排序
    print("l2:", l2)

    # 增删改查
    l2.append(100)
    print(l2)
    l2.insert(0, "many")
    print(l2)

    l2[0:2] = [] # 大于一个元素
    print(l2)

    l2.pop(1) # 删除指定索引的元素，默认是-1
    print("pop:", l2)
    l2.remove(100) # 根据元素删除
    print("remove",l2)


    l2[0] = "afternoon"
    print(l2)

    # 逆序
    l2.reverse()
    print(l2)

    # 浅copy 内存一份，多了个引用
    l3 = l2
    print(l3)
    l2[0] = "change"
    print(l3)

    # 深copy 内存两份
    l3 = l2[:]
    print(l3)
    l2[0] = "change again"
    print(l3)

    l4 = l3.copy()
    print("l3:", l3)
    print("l4:", l4)
    l3[0] = "copy"
    print("l3:", l3)
    print("l4:", l4)

def tupleTest():
    '''元祖的基本用法: + in not in *n [] .index() .count() max() min() len()'''
    t = (1,)
    print(type(t))

def setTest():
    '''集合类型:可变，不重复, 无序'''
    st = set(range(10))
    print(st)
    l = list(set([1,2,3,1,2,3,33,1,3]))
    print(l)

    for s in st:
        print(s)

def dictTest():
    '''字典:映射 {key1:value1, key2:value2} key不可变类型'''
    d = {'name':'python','age':22,1:[1,2,3], (1,2):"test"}
    print(d)
    d2 = dict(mon=1,tue=2,fri=5,sat=6)
    print(d2)

    for k in d:
        print(d[k])

    print(d.keys(), d.values(), d.items())

    # 添加新成员
    d2.update(wed=3, thr=4, sun=7)
    print(d2)

if __name__ == '__main__':
    #listTest()
    #strTest()
    #tupleTest()
    #setTest()
    dictTest()

    # bytes
    s = "中国\n"
    print(s, len(s))

    s3 = r"中国\n"
    print(s3, len(s3))

    # ascii
    s2 = b'hello'
    print(s2)





