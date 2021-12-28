from pymongo import MongoClient
import os
import sys
texts=[]
with open(sys.argv[1]) as f:
	for line in f:
		items=line.strip().split('\t')
		texts.append({"text":items[0],"score":int(items[1])})
print('load %d lines' % len(texts))
client=MongoClient('localhost',27017)
db=client.student
collection=db.comments
result=collection.insert_many(texts)
print(result)
client.close()


