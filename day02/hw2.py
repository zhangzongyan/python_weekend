# -*- coding: utf-8 -*-
#   File Name：     hw2
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19

import random
import time
import sys

FRUITLIST = ["苹果", "梨", "香蕉", "火龙果", "李子", "桃子"]

def show():
    for f in FRUITLIST:
        print(f, end=" ")
    print()


def main():
    # 打印水果
    show()

    print("请注意看以下水果的顺序:")
    index = []
    for i in range(3):
        # 选择三个水果输出
        index.append(random.randint(0, len(FRUITLIST)-1))
        print("\r", "第%d个"%(i+1), FRUITLIST[index[i]], end="")
        sys.stdout.flush()
        time.sleep(1)
        index[i] += 1 # 用户输入序号从1开始的

    print()
    # 等待游戏者输入顺序
    user_seq = input("请将你看到的水果的顺序，按照序列号依次输入:")
    # 校验输入顺序是否正确

    user_seq = list(map(int,user_seq))
    if user_seq == index:
        print("回答正确！太聪明了")
    else:
        print("很遗憾！下次要认真看")

if __name__ == '__main__':
    main()
