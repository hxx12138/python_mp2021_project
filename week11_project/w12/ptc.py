from multiprocessing import Process
from threading import Thread
import os,time,random

def dense_cal():
    res=0
    for i in range(100000000):
        res*=i

def dense_io():
    time.sleep(2)#simulate the io delay

def diff_pt(P=True,pn=4,target=dense_cal):
    tlist=[]
    start=time.time()
    for i in range(pn):
        if P:
            p=Process(target=target)
        else:
            p=Thread(target=target)
        tlist.append(p)
        p.start()
    for p in tlist:
        p.join()
    stop=time.time()
    if P:
        name='multi-process'
    else:
        name='multi-thread'
    print('%s run time is %s' %(name,stop-start))

if __name__=='__main__':
    diff_pt(P=True)
    diff_pt(P=False)
    
    diff_pt(P=True,pn=100,target=dense_io)
    diff_pt(P=False,pn=100,target=dense_io)