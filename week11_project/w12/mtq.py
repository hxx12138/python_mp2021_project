from threading import Thread,currentThread
import queue
import random
import time

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        time.sleep(random.randint(1,2))
        print("%s get %s" %(currentThread().name,item))
        q.task_done()

num_worker_threads=10

q = queue.Queue()
threads = []
for i in range(10):
    t = Thread(target=worker)
    threads.append(t)
    t.start()
    

for item in "abcdefghijklmnopqrstuvwxyz0123456789":
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()