from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import current_process
import matplotlib.pyplot as plt
import os
import time

global_result=[]

def fib(max):
	n,a,b=0,0,1
	while n<max:
		a,b=b,a+b
		n+=1
	return b

def job(n):
	print('{} is working on {}...'.format(os.getpid(),n))
	time.sleep(2)
	return fib(n)

def add_result(res):#callback func
	global global_result
	print("called by {}, result is {}".format(current_process().pid,res))
	#也可以返回进程标识信息，用以识别结果（比如进程的参数）
	#可以用字典存储
	global_result.append(res)

def add_result_map(res):
	global global_result
	print("called by {}, result is {}".format(current_process().pid,res))
	for r in res:
		global_result.append(r)

if __name__=='__main__':
	p=Pool()#cpu determines
	ms=range(1,20)
	results=[]
	#同步调用
	#创建多个进程，但是只有一个执行，需要等到执行结束后再可以返结果
	#并不并行
	'''for m in ms:
		print('{} will be applied in main'.format(m))
		res=p.apply(job,args=(m,))#会等待执行结束后再执行下一个
		print(res)
		print('{} is applied in main'.format(m))
		results.append(res)
	p.close()#!!！
	print(results)
	plt.figure()
	plt.plot(ms,results)
	plt.show()
	plt.close()'''
	
	#异步调用
	#可以并行
	'''for m in ms:
		res=p.apply_async(job,args=(m,))#注意这里res只是一个引用
		results.append(res)
		#如果马上打印，可能并没有结果
		print(res)
	p.close()
	p.join()
	results2=[]
	for res in results:
		results2.append(res.get())
	print(results2)
	plt.figure()
	plt.plot(ms,results2)
	plt.show()
	plt.close()'''

	#callback
	'''for m in ms:
		p.apply_async(job,args=(m,),callback=add_result)
		#callback函数只有一个参数
		#callback函数是由主进程执行的
	p.close()
	p.join()
	plt.figure()
	plt.plot(ms,sorted(global_result))#顺序可能是乱的，这里可以排序解决，但其他问题不一定
	plt.show()
	plt.close()'''


	#使用map
	'''results3=p.map(job,ms)
	print(type(results3))#list
	p.close()
	plt.figure()
	plt.plot(ms,results3)
	plt.show()
	plt.close()'''

	#使用map_async
	'''p.map_async(job,ms,callback=add_result_map)
	p.close()
	p.join()
	plt.figure()
	print(len(ms))
	print(len(global_result))
	plt.plot(ms,global_result)
	plt.show()
	plt.close()'''