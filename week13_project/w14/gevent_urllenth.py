import gevent,time
from gevent import monkey
#标记IO非阻塞，针对标准库
monkey.patch_all()  

from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def url_request(url):
    print('get:%s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%s KB received from %s'%(len(data)//(1024*8),url))

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(url_request,'https://www.python.org'),
    gevent.spawn(url_request,'https://www.buaa.edu.cn'),
    gevent.spawn(url_request,'https://www.163.com'),
])
print(time.time()-async_time_start)