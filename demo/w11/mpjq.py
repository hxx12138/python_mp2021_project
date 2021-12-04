from multiprocessing import Process
from multiprocessing import JoinableQueue
import time
import random
import os

class Product:
	def __init__(self,name,volume):
		self._name=name
		self._volume=volume
	def __str__(self):
		return "Name:{}\tVolume:{}".format(self._name,self._volume)

def consume(q):
	print(f"consumer {os.getpid()} started...")
	prod=q.get()
	time.sleep(random.randint(1,5))
	print("{} consumes {}".format(os.getpid(),prod))
	q.task_done()#发送信号，表明数据获取成功

def produce(q):
	print(f"producer {os.getpid()} started...")
	prod=Product(str(os.getpid())+"_pro",random.randint(10,100))
	time.sleep(random.randint(1,5))
	q.put(prod)
	print("{} produces {}".format(os.getpid(),prod))
	q.join()

if __name__=='__main__':
	q=JoinableQueue()
	producers=[]
	consumers=[]
	for i in range(0,2):
		p=Process(target=produce,args=(q,))
		producers.append(p)
	for i in range(0,100):
		c=Process(target=consume,args=(q,))
		c.daemon=True #必要，否则部分消费者进程并不退出
		consumers.append(c)
	for c in consumers:
		c.start()
	for p in producers:
		p.start()
	for p in producers:
		p.join()
	print('main')