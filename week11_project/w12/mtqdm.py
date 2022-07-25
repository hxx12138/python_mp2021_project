import concurrent.futures
import random
import tqdm
import time
import sys

def task(x):
	time.sleep(x*0.1)
	return x

def download_many(count):
	with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
		todomap=[]
		for x in range(100):
			future=executor.submit(task,x)
			todomap.append(future)
		dointer=concurrent.futures.as_completed(todomap)
		dointer=tqdm.tqdm(dointer,total=len(todomap))
		for future in dointer:
			res=future.result()

if __name__=='__main__':
	download_many(int(sys.argv[1]))
