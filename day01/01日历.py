# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01日历
   Description :
   Author :       zongyanzhang
   date：          2018/8/12
-------------------------------------------------
   Change Activity:
                   2018/8/12:
-------------------------------------------------
"""
__author__ = 'admin'

'''
读入用户输入的年月: 1998/3
已知1990.1.1是星期一
问用户输入的日期对应的日历

分析：
    1.1998.3.1是星期几
    2.1998.3月有多少天
'''
YEAR = 1990
# 判断是平年还是闰年
def isleap(year):
    '''是否为闰年，是True,否False'''
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# 任意一年的任意一月有多少天
def dayofmonth(month, year):
    ret = -1
    if month in [1,3,5,7,8,10,12]:
        ret = 31
    elif month in [4,6,9,11]:
        ret = 30
    elif month == 2:
        ret = 28 + isleap(year)
    else:
        pass

    return ret

def main():
    # 读入用户输入 假定1998/3 "1998,3"
    year, month = eval(input("请输入年月(y,m):"))
    sumdays = 0 # 总天数

    # 1990~1998天数
    for y in range(YEAR, year):
        sumdays += (365+isleap(y)) # sumdays = sumdays + (365+isleap(y))

    # 1998.1.1 ~ 1998.3.1天数
    for m in range(1, month):
        sumdays += dayofmonth(m, year)
    sumdays += 1 # month.1

    # 总天数 % 7----》星期几
    week = sumdays % 7
    print("{}/{}/1是星期{}". format(year, month, week))

    # 求出1998.3月有多少天
    days = dayofmonth(month, year)

    # 打印输出
    s = "{}年{}月".format(year, month)
    print(s.center(28))
    print("sun mon thu wed thr fri sat")
    # 打印出1号是星期几相应的空格
    print("    "*week, end="")
    for d in range(1, days+1):
        print("%3d" % d, end=" " if (d+week) % 7 != 0 else "\n")
    print()


if __name__ == '__main__':
    main()

