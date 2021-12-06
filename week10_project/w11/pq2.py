from multiprocessing import Process, Queue, JoinableQueue
import random
import time
import os

def consume(q):
	item=q.get()
	if item is None:
		return
	else:
		print('{} get {} from queue'.format(os.getpid(),item))
		q.task_done()

def produce(q):
	item=random.random()
	time.sleep(item)
	q.put(item)
	print("{} put {} into queue".format(os.getpid(),item))
	q.join()
	print("in {} join q finishes".format(os.getpid()))

if __name__=='__main__':
	q=JoinableQueue()
	plist=[]
	clist=[]
	for i in range(10):
		plist.append(Process(target=produce,args=(q,)))
	for i in range(20):
		clist.append(Process(target=consume,args=(q,)))
	for p in plist:
		p.start()
	for c in clist:
		c.start()
	for p in plist:
		p.join()
	#发送None是必要的
	for c in clist:
		q.put(None)
	for c in clist:
		c.join()

	# in main
	print("in main, all processes ends...")
