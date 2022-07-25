from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import Array
import sys

class Counter(Process):

	def __init__(self,id,name,counter,checkin):
		super().__init__()
		self._id=id
		self._name=name
		self._counter=counter
		self._checkin=checkin


	def run(self):
		with self._counter.get_lock():#large number of process will trigger error
			self._counter.value+=1
		print('{} update counter to {}'.format(self._name,self._counter.value))
		self._checkin[self._id]=1


if __name__=='__main__':
	num_processes=int(sys.argv[1])
	counter=Value('i',0,lock=True)
	checkin=Array('i',num_processes,lock=True)
	clist=[]
	for i in range(num_processes):
		c=Counter(i,'counter-{}'.format(i),counter,checkin)
		clist.append(c)
	for c in clist:
		c.start()
	for c in clist:
		c.join()
	print('child processes end...')
	print('in the main process, counter.value={}'.format(counter.value))
	for ck in checkin:
		print(ck,end=' ')
	print('')