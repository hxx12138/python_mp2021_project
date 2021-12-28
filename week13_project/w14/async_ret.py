import asyncio
import random

async def get_page(url,i):
	#print("start visit {}".format(url))
	await asyncio.sleep(random.randint(1,10))#nio
	#print("get the html page")
	return i

def print_status(future):#指定回调函数，运行结束后马上处理
	print("%s" % future.result(),end=' ')

if __name__=='__main__':
	loop=asyncio.get_event_loop()
	tasks=[]
	for i in range(100):
		tasks.append(loop.create_task(get_page('www.baidu.com/',i)))
	for task in tasks:
		task.add_done_callback(print_status)#注意与执行顺序的不同，等所有任务执行结束后再获取结果
	loop.run_until_complete(asyncio.wait(tasks))
	
	print()
	
	for task in tasks:
		print(task.result(),end=' ')

	print()
