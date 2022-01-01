import pymongo
from pymongo import collection

client = pymongo.MongoClient("mongodb+srv://hxx:hexihexiang2000@cluster0.amu8k.mongodb.net/student?retryWrites=true&w=majority")

db = client['info']
collections_1 = db['week_1']
#collections_2 = db['week_2']

doc_list_1 = collections_1.find().sort('排名')
for doc in doc_list_1:
    if doc['排名'] != 0:
        print(doc)
