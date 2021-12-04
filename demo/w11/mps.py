from multiprocessing import Process
from multiprocessing import Semaphore
from multiprocessing import current_process
import time
import random

def get_connections(s):
	s.acquire()
	try:
		print(current_process().name+' acqiure a connection')
		time.sleep(random.randint(1,2))
		print(current_process().name+' finishes its job and return the connection')
	except:
		raise
	finally:
		s.release()

if __name__=='__main__':
	connections=Semaphore(5)
	workers=[]
	for i in range(20):
		p=Process(target=get_connections,args=(connections,),name='worker:'+str(i+1))
		workers.append(p)
	for p in workers:
		p.start()
	for p in workers:
		p.join()
	print("all workers exit")
	