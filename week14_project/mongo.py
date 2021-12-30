import pymongo
from pymongo import collection
import pandas as pd


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


df = pd.read_csv('week_1/21.csv')
title = list(df)
#print(title)

data_list = []
