# -*- coding: utf-8 -*-
#   File Name：     hw1
#   Description :
#   Author :       zongyanzhang
#   date：          2018/8/19
#################################

USER = "root"
PASSWORD = "python123"

def main():
    error_cnt = 0
    flag_user = True

    while error_cnt < 3:
        if flag_user:
            user = input("用户:")
        password = input("密码:")
        if user != USER:
            print("此用户不存在，请重新输入")
            error_cnt += 1
        else:
            if password != PASSWORD:
                print("密码错误请重新输入")
                flag_user = False
                error_cnt += 1
            else:
                print("登录成功")
                break
    else:
        # 循环条件为假
        print("鉴定错误")

if __name__ == '__main__':
    main()











