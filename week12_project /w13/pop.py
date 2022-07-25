from poplib import POP3_SSL
from email.parser import Parser

pop3_server='pop.qq.com'
port=995
user='jichang.zhao@qq.com'
passwd='jmxflofuugodbgga'

server=POP3_SSL(pop3_server, port)
print("服务器连接成功")
print(server.getwelcome())
server.user(user)
print("用户名正确")
server.pass_(passwd)
print("密码正确")
print('#Emails: %s. Size: %s' % server.stat())
resp, mails, octets=server.list()
for i in range(1,len(mails)+1):
	resp,lines,octets=server.retr(i)
	content=b'\r\n'.join(lines).decode('utf-8')
	message=Parser().parsestr(content)
	print(message)
	print('------------------')
server.close()