from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.utils import parseaddr, formataddr
from smtplib import SMTP_SSL

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

smtp_server='smtp.qq.com'
port=465
from_addr='jichang.zhao@qq.com'
passwd='jmxflofuugodbgga'
to_addr='liyashuai@buaa.edu.cn'

message=MIMEMultipart()
message['From']=_format_addr('李亚帅<%s>' % from_addr)
message['To']= _format_addr('北航MBA校友会<%s>' % to_addr)
message['Subject']=Header('校友会换届通知', 'utf-8').encode()

#正文
message.attach(MIMEText('如下<strong>附件</strong>分别是这次换届的通知。请查收。','html','utf-8'))

#附件1
textfile=MIMEText(open('smtp.py','rb').read(),'base64','utf-8')
textfile['Content-Type']='application/octet-stream'
textfile['Content-Disposition']='attachment; filename="smtp.py"'
message.attach(textfile)

#附件2
picfile=MIMEImage(open('y.jpeg', 'rb').read())
picfile.add_header('Content-Disposition', 'attachment', filename="y.jpeg") 
message.attach(picfile)

#附件3
docfile=MIMEApplication(open('test.docx','rb').read()) 
docfile.add_header('Content-Disposition', 'attachment', filename="test.docx") 
message.attach(docfile) 

server=SMTP_SSL(smtp_server,port)
server.login(from_addr, passwd)
print('登录成功')
print("邮件开始发送")
server.sendmail(from_addr, [to_addr], message.as_string())
server.quit()
print("邮件发送成功")
