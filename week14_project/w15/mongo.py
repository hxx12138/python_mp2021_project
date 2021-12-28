import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
for db in dblist:
	print(db)
mydb = myclient["student"]
mycol = mydb["comments"]
myclient.close()