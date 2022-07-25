from multiprocessing import Process
from multiprocessing import Event
import time
import random

def car(event,name):
	while True:
		if event.is_set():
			time.sleep(random.random())
			print("car {} passes...".format(name))
			break
		else:
			print("car {} waits...".format(name))
			event.wait()#阻塞直至事件状态发生变化

def light(event):
	while True:
		if event.is_set():
			event.clear()
			print("红灯")
			time.sleep(random.random())
		else:
			event.set()
			print("绿灯")
			time.sleep(random.random())

if __name__=='__main__':
	event=Event()
	event.clear()
	l=Process(target=light,args=(event,))
	l.daemon=True
	l.start()
	cars=[]
	for i in range(10):
		c=Process(target=car,args=(event,'c_'+str(i+1)))
		cars.append(c)
	for c in cars:
		c.start()
	for c in cars:
		c.join()
	print("all cars passed...")