import gevent
from gevent import monkey, pool
#patch十分必要，否则无法体现协程的优势（io是阻塞的）
monkey.patch_all()
#十分神奇，但一定要注意，先import gevent，完了提前进行monkey.patch_all()，之后再引入其他模块

from bs4 import BeautifulSoup
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

jobs = []

p = pool.Pool(10)#控制数目

urls = ['https://www.163.com','https://www.baidu.com','https://www.qq.com','https://www.buaa.edu.cn','https://www.apple.com.cn']

def get_links(url):
    links=set()
    print("load url of %s" % url)
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'lxml')
        for a in soup.find_all('a'):
            if 'href' in a.attrs:
                if a['href'].find('http://')>=0:
                    links.add(a['href'])
    return len(links)

for url in urls:
    jobs.append(p.spawn(get_links, url))
gevent.joinall(jobs)
for url, links in zip(urls,[job.value for job in jobs]):
	print("%s\t%s" % (url,links))