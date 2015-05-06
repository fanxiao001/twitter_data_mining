# -*- encoding: utf-8 -*-
'''
Created on 2015年5月6日

@author: xiao
@summary: MongoDb connection
'''
from pymongo import MongoClient
from datetime import datetime

def getMongoDBClient(address=''):
    if not address:
        client=MongoClient()
    else:
        client = MongoClient(address)
    return client

def getDB(client,database):
    db=client[database]
    return db
def insertDocument(db,collection,content):
    result=db[collection].insert_one(content)
    return result.inserted_id

#client=getMongoDBClient()
#db=getDB(client, 'test')
#result=db.collection.delete_many({})

