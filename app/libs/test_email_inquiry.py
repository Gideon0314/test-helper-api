# -*- coding: UTF-8 -*-
import smtplib
import yagmail
from config import INQUIRY_EMAIL, INQUIRY_EMAIL_PW, INQUIRY_EMAIL_LIST


def send_email(recipient, headline, contents):
    yag = yagmail.SMTP(user=INQUIRY_EMAIL, password=INQUIRY_EMAIL_PW, host='smtp.126.com')
    return yag.send(recipient, headline, contents)


def email_inquiry():
    import time
    recipient = INQUIRY_EMAIL_LIST
    time = time.time()
    headline = f'全球赢-技术部-询盘{time}'
    contents = f'全球赢-技术部-询盘测试{time}'

    try:
        send_email(recipient, headline, contents)
        print('定时邮件询盘发送成功，请验收')
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def warning_email():
    try:
        send_email('gideon_tao@skytech.cn', '询盘发送定时任务异常报警', '询盘发送定时任务异常报警，请及时处理')
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
