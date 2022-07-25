from threading import Thread, Barrier,currentThread
import time
import random

b=Barrier(5, timeout=5)

def server():
	b.wait()
	print('一桌凑齐，开麻...')

def client():
	time.sleep(random.randint(1,4))
	print('%s 入桌' % currentThread().name)
	b.wait()

Thread(target=server).start()

for i in range(4):
	c=Thread(target=client,name="client-"+str((i+1)))
	c.start()
