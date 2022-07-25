from pymongo import MongoClient
with MongoClient('localhost',27017) as client:
	db=client.student
	collection=db.comments

	docs=collection.find({"text":{"$regex":"开机"}}).sort("score",1)
	for doc in docs:
		print(doc['text'], doc['score'])