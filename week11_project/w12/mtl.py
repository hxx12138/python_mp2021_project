from threading import Thread
import threading
import random
import time

class Runner(Thread):
	def __init__(self,name,timer,stime):
		super().__init__()
		self._name=name
		self._timer=timer
		self._stime=stime

	def run(self):
		self._timer.start=self._stime
		time.sleep(random.randint(1,3))
		print('in {}, timer starts since {}'.format(self._name,self._timer.start))


if __name__=='__main__':
	timer=threading.local()
	timer.start=0
	tlist=[]
	for i in range(10):
		r=Runner('thread-{}'.format(i),timer,random.randint(1,100))
		tlist.append(r)
	for r in tlist:
		r.start()
	for r in tlist:
		r.join()
	print('child threads end')
	print('in main thread, timer.start={}'.format(timer.start))
