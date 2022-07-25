from multiprocessing import Process, Queue
import time
import random
import os

def produce(q):
	time.sleep(random.random())
	q.put('car_by_{}'.format(os.getpid()))
	print("{} produces a car...".format(os.getpid()))

def buy(q):
	car=q.get()
	if car is None:
		print("no car. {} ends.".format(os.getpid()))
		return
	else:
		time.sleep(random.random())
		print("{} buy the car {}".format(os.getpid(),car))

if __name__=='__main__':
	q=Queue()
	procucers=[]
	consumers=[]
	for i in range(0,2):
		p=Process(target=produce,args=(q,))
		procucers.append(p)
	for i in range(0,100):
		c=Process(target=buy,args=(q,))
		consumers.append(c)
	for p in procucers:
		p.start()
	for p in procucers:
		p.join()
	for c in consumers:
		c.start()
	for c in consumers:
		q.put(None)#主进程发信号结束，但要给每一个consumer准备
	print('main')