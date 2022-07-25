import time
import random
from multiprocessing import Process

n=0

def task(name):
	print("task of {} starts".format(name))
	time.sleep(random.randrange(50,100))
	print("task of {} ends".format(name))

class Task(Process):
	def __init__(self,name):
		super().__init__()#不能忘了
		self._name=name

	@property
	def name(self):
		return self._name

	def run(self):#不能忘了
		print('task {} starts with pid {}...'.format(self.name,self.pid))
		global n
		n=random.random()
		print("n={} in process {}".format(n,self.name))
		#mem
		l=list(range(int(n*100000000)))#观察内存的不同
		time.sleep(random.randrange(20,50))
		print('task {} ends with pid {}...'.format(self.name,self.pid))
	

if __name__=='__main__':
	'''for i in range(0,4):
		p=Process(target=task,args=('task {}'.format(i),))
		p.start()
		print('pid:{}'.format(p.pid))'''
	plist=[]
	for i in range(0,4):
		p=Task('process-{}'.format(i+1))
		plist.append(p)	
	for p in plist:
		p.start()
	for p in plist:
		#注意一定是先子进程都启动后，再一一join，否则启动后马上join会变成“串行”
		#1. 是的，这样写join仍然会卡着等p1运行结束，但其他进程如p2, p3等仍在运行，等p1运行结束后，循环继续，p2,p3等可能也运行结束了，会迅速完成join的检验
		#2. join花费的总时间仍然是耗费时间最长的那个进程运行的时间，这样跟我们的目的是一致的。
		pass
		p.join()
	print('main')
	print("n={} in main".format(n))