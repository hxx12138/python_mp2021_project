from threading import Thread,currentThread
import time

def task(name):
    time.sleep(2)
    print('%s print name: %s' %(currentThread().name,name))

class Task(Thread):
    def __init__(self,name):
        super().__init__()
        self._name=name
    
    def run(self):
        time.sleep(2)
        print('%s print name: %s' % (currentThread().name,self._name))

if __name__ == '__main__':
    n=100
    var='test'
    t=Thread(target=task,args=('thread_task_func',))
    t.start()
    t.join()

    t=Task('thread_task_class')
    t.start()
    t.join()
    
    print('main')