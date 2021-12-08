from multiprocessing import Process
from multiprocessing import Value

class Counter(Process):

	def __init__(self,id,name,counter,checkin):
		super().__init__(self)
		self._id=id
		self._name=name
		self._counter=counter
		self._checkin=checkin


	def run(self):
		#with self._counter.get_lock():
		self._counter.value+=1
		self._checkin[self._id]=1


if __name__=='__main__':

	num_processes=10
	counter=Value(int,0,lock=True)
	checkin=Array(int,num_processes,lock=True)
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
	print('the check-in status: {}'.format('-'.join(str(checkin[i])) for i in range(num_processes)))