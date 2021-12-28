import gevent
from gevent import socket#asyncio

urls=['www.apple.com.cn','www.buaa.edu.cn','www.google.com','www.baidu.com']
jobs=[gevent.spawn(socket.gethostbyname,url) for url in urls]
gevent.joinall(jobs,timeout=10)
for url,ip in zip(urls,[job.value for job in jobs]):
	print('{}\t{}'.format(url,ip))


