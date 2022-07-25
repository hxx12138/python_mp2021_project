import pymongo
from pymongo import collection


client = pymongo.MongoClient("mongodb+srv://hxx:hexihexiang2000@cluster0.amu8k.mongodb.net/student?retryWrites=true&w=majority")

db = client['info']
collections = db['content']
#mydict = { "name": "Google", "alexa": "1", "url": "https://www.google.com" }
#x = collections.insert_one(mydict)

#print(db)
db_list = client.list_database_names()
print(db_list)
x = collections.find_one()
print(x)



'''print(db)
dblist = client.list_database_names()
for db in dblist:
	print(db)'''
'''myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
for db in dblist:
	print(db)
mydb = myclient["student"]
mycol = mydb["comments"]
myclient.close()'''