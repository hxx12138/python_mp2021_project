from multiprocessing import Process
from multiprocessing import Lock
import json
import random
import time

tf='ticks.json'

def info():
	ticks=json.load(open(tf))
	print("ticks from {} to {} left {}".format(ticks['origin'],ticks['dest'],ticks['count']))

def buy(pname):
	ticks=json.load(open(tf))
	time.sleep(random.random())
	if ticks['count']>0:
		ticks['count']-=1
		time.sleep(random.random())
		json.dump(ticks,open(tf,'w'))
		print('{} buy one tick from {} to {}!'.format(pname,ticks['origin'],ticks['dest']))
	else:
		print('oh....no ticks :(')

def task(pname):
	info()
	buy(pname)

#加锁
def lock_task(name,lock):
	info()
	lock.acquire()
	try:
		buy(name)
	except:
		raise
	finally:
		lock.release()

if __name__=='__main__':
	lock=Lock()
	clients=[]
	for i in range(20):
		name='client-{}'.format(i+1)
		#p=Process(target=task,name=name,args=(name,))
		p=Process(target=lock_task,name=name,args=(name,lock))
		clients.append(p)
	for p in clients:
		p.start()
	for p in clients:
		p.join()
	print("all clients finished...")
