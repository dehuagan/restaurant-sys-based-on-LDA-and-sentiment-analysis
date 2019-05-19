# coding=utf-8
import smtplib
import random
from email.mime.text import MIMEText
def email_validation(target_email):
    msg_from = '958256592@qq.com'  # 发送方邮箱
    passwd = 'lzqhusvftonbbedd'  # 填入发送方邮箱的授权码
    msg_to = target_email  # 收件人邮箱

    subject = "pa邮箱验证码"  # 主题
    validation_num = random.randint(100000,999999)
    content = '您的pa系统邮箱验证码为：'+str(validation_num)# 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)# 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        return (1,validation_num)
    except s.SMTPException, e:
        return (0,validation_num)
    finally:
        s.quit()

