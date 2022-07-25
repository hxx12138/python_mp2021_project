import time
import jieba
import pickle
import pandas as pd
from multiprocessing import Process,Queue
def fenci(p,q,stoplist,sentencelist):
    start=time.time()
    counts={}
    for i in sentencelist:
        words=jieba.cut(i)
        for j in words:
            if j not in stoplist:
                if j not in counts:
                    counts[j] = 1
                else:
                    counts[j] +=1
    with open ('wh/process'+str(p)+'-'+str(q)+'.pkl','wb') as f:
        pickle.dump(counts,f)
    over=time.time()
    print(f"{p}个进程，the no.{q} process use {over-start}s")

def reduce(dic1,dic2):
    for key,value in dic2.items():
        if key in dic1:
            dic1[key]+=value
        else :
            dic1[key]=value
    return dic1

if __name__=='__main__':
    '''start=time.time()
    f=open('news_sohusite_xml.dat',encoding='gb18030')
    contentlist=[]
    plist=[]
    for line in f:
        if line[0:9]=='<content>':
            contentlist.append(line.strip('<content>'))
    f.close()
    fpp=open('stopwords_list.txt','r',encoding='utf-8')
    stoplist=[]
    while 1:
        word=fpp.readline()
        word=word.strip('\n')
        word=word.strip('  ')
        if (word!=''):
            stoplist.append(word)
        else:
            break
    fpp.close()
    x=len(contentlist)//6
    totallist=[]
    for i in range(6):
        totallist.append(contentlist[x*i:x*(i+1)])
    plist=[]
    for i in range(6):
        p=Process(target=fenci,args=(6,i,stoplist,totallist[i]))
        plist.append(p)
    for p in plist:
        p.start()
    for p in plist:
        p.join()
    over6=time.time()
    print('6个进程总时间：',over6-start)'''
    totaldic={}
    with open('process6-0.pkl','rb')as f:
        totaldic=pickle.load(f)
    for i in range(1,6):
        with open('process6-'+str(i)+'.pkl','rb') as f:
            dic1=pickle.load(f)
            totaldic=reduce(totaldic,dic1)
            f.close()
    with open ('process6-total.pkl','wb') as f:
        pickle.dump(totaldic,f)
            
        
    
