import sys
from pymongo import MongoClient

#0 差评；1 好评;

with MongoClient('localhost',27017) as client:
	db=client.student
	collection=db.comments

	re=collection.find_one()
	re=collection.find_one({"score":1})
	if 'text' in re:
		print(re['text'])
	res=collection.find({"score":int(sys.argv[1])}).limit(5)
	for index, doc in enumerate(res,start=1):
		if 'text' in doc and 'score' in doc:
			print(index,doc['score'],doc['text'])
