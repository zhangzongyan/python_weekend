# -*- coding: utf-8 -*-
#   File Name：     09_枚举类
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19
from enum import Enum, unique

# DAY = 100

@unique
class Weekday(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THR = 4
    FRI = 5
    SAT = 6
    SUN = 7
    # DAY = 5 @unique 确保枚举类中所有值不重复
# 枚举的多个值不能改变---》常量


print(Weekday.MON.value)
print(Weekday['MON'])

# 遍历
for name, member in Weekday.__members__.items():
    print(name, member)