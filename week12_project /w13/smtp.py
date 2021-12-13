from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP, SMTP_SSL

smtp_server='smtp.qq.com'
port=465
from_addr='jichang.zhao@qq.com'
passwd='jmxflofuugodbgga'
to_addr='jichang@buaa.edu.cn'

message=MIMEText('明天中午12点在A939开会。务必准时参加。', 'plain', 'utf-8')
message['From']=Header(from_addr, 'utf-8')
message['To']= Header("现代程序设计", 'utf-8')
message['Subject'] = Header('会议通知', 'utf-8')

server=SMTP_SSL(smtp_server,port)
server.login(from_addr, passwd)
print('登录成功')
print("邮件开始发送")
server.sendmail(from_addr, [to_addr], message.as_string())
server.quit()
print("邮件发送成功")