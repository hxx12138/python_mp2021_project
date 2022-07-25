from pymongo import MongoClient
with MongoClient('localhost',27017) as client:
	db=client.student
	collection=db.comments

	c=collection.count_documents({"text":{"$regex":"机箱"}})
	print(c)
	docs=collection.find({"text":{"$regex":"机箱"}})
	for doc in docs:
		print(doc['text'])