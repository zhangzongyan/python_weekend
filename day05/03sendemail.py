# -*- coding: utf-8 -*-
#   File Name：     03sendemail
#   Description :
#   Author :       zongyanzhang
#   date：          2018/9/16
"""
邮件发送:
    email
        邮件文本
    stmplib
        发送邮件
"""
import smtplib
from email.mime.text import MIMEText

# 构建邮件正文
def write_text():
    msg = MIMEText("我不是广告", 'plain', 'utf-8')
    msg['From'] = '{}'.format("python_1989@163.com") # 发送者
    msg['To'] = '{}'.format('python_1989@sina.com') # 接受者
    msg['Subject'] = 'hello' # 主题
    return msg.as_string() # 转字符串


# 连接服务器
smtp = smtplib.SMTP('smtp.163.com', 25)
smtp.set_debuglevel(True) # 打开调试

# 登录
try:
    smtp.login("python_1989@163.com", "python999")

except Exception as e:
    print("失败了:{}".format(e))

# 邮件发送
smtp.sendmail("python_1989@163.com", ["python_1989@sina.com", "python_1989@163.com", "1754590066@qq.com"], write_text())
smtp.quit()


