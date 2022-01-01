import pymongo
from pymongo import collection
import pandas as pd
import datetime
import pickle

client = pymongo.MongoClient("mongodb+srv://hxx:hexihexiang2000@cluster0.amu8k.mongodb.net/student?retryWrites=true&w=majority")

db = client['info']
collections_1 = db['week_1']
collections_2 = db['week_2']
#mydict = { "name": "Google", "alexa": "1", "url": "https://www.google.com" }
#x = collections.insert_one(mydict)

#print(db)
db_list = client.list_database_names()
print(db_list)
#x = collections.find_one()
#print(x)

#print(datetime.datetime.now())

'''data_list_1 = [{'分区号':0, '排名':0, 'BV号':0, '时长':0, '播放量':0, '弹幕':0, '标题':0, '封面':0, '评论':0, '收藏':0, '描述':0, '直链':0, '时间':0} for i in range(10001)]
df_1 = pd.read_csv('week_1/21.csv')
title_1 = list(df_1)
print(title_1)
for i in range(len(title_1)):
    print(f'the no.{i} col has completed.')
    for j in range(len(list(df_1[title_1[i]]))):
        data_list_1[j][title_1[i]] = list(df_1[title_1[i]])[j]
#print(data_list_1)

for i in range(len(data_list_1)):
    print(f'insert no.{i+1}')
    date = datetime.datetime.now()
    data_list_1[i]['时间'] = date
    doc = collections_1.insert_one(data_list_1[i])
x = collections_1.find_one()
print(x)

data_list_2 = [{'分区号':0, '排名':0, 'BV号':0, '时长':0, '播放量':0, '弹幕':0, '标题':0, '封面':0, '评论':0, '收藏':0, '描述':0, '直链':0, '时间':0} for i in range(10001)]
df_2 = pd.read_csv('week_2/21.csv')
title_2 = list(df_2)
print(title_2)
for i in range(len(title_2)):
    print(f'the no.{i} col has completed.')
    for j in range(len(list(df_2[title_2[i]]))):
        data_list_2[j][title_1[i]] = list(df_2[title_2[i]])[j]
#print(data_list_2)

for i in range(len(data_list_2)):
    print(f'insert no.{i+1}')
    date = datetime.datetime.now()
    data_list_2[i]['时间'] = date
    doc = collections_2.insert_one(data_list_1[i])
x = collections_2.find_one()
print(x)'''

week_1_list = collections_1.find()
'''with open('week_1/week_1_origin.pkl','wb') as f:
    pickle.dump(list(week_1_list),f)'''

i = 0
week_2_list = collections_2.find()
for info_2 in week_2_list:
    print(f'the no.{i+1} has completed.')
    i += 1
    bv = info_2['BV号']
    query = {'BV号':bv}
    if (collections_1.find(query)):
        update_dict = {'$set':collections_1.find(query)[0]}
        collections_1.update_one(query,update_dict)
    else:
        collections_1.insert_one(info_2)

week_1_list = collections_1.find()
'''with open('week_1/week_1_update.pkl','wb') as f:
    pickle.dump(list(week_1_list),f)'''
