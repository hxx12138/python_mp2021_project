from threading import Thread, Condition,currentThread
import time
import random

con=Condition()
q=list()

def check_q():
	return len(q)

def consume():
	with con:
		con.wait_for(check_q)
		print("%s consume %s" %(currentThread().name,q.pop()))

def produce():
	with con:
		for i in range(2):
			q.append(random.random())
		con.notify_all()

clist=[]
for i in range(20):
	c=Thread(target=consume,name='c-'+str(i+1))
	clist.append(c)
plist=[]
for i in range(20):
	p=Thread(target=produce,name='p-'+str(i+1))
	plist.append(p)
for c in clist:
	c.start()
for p in plist:
	p.start()