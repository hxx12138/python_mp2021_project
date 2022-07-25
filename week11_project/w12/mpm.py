from multiprocessing import Process
from multiprocessing import Manager, Lock
import time
import random


def register(d,name):
	if name in d:
		print('duplicated name found...register anyway...')
		d[name]+=1
	else:
		d[name]=1
	time.sleep(random.random())

def register_with_loc(d,name,lock):
	with lock:
		if name in d:
			print('duplicated name found...register anyway...')
			d[name]+=1
		else:
			d[name]=1
	time.sleep(random.random())
	

if __name__=='__main__':
	#Manager
	names=['Amy','Lily','Dirk','Lily', 'Denial','Amy','Amy','Amy']
	manager=Manager()
	dic=manager.dict()
	lock=Lock()
	#manager.list()
	students=[]
	for i in range(len(names)):
		#s=Process(target=register,args=(dic,names[i]))
		s=Process(target=register_with_loc,args=(dic,names[i],lock))
		students.append(s)
	for s in students:
		s.start()
	for s in students:
		s.join()
	print('all processes ended...')
	for k,v in dic.items():
		print("{}\t{}".format(k,v))