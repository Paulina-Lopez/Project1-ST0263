# src/database/database.py

from pymongo import MongoClient

def connect(collection):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["DFS_DB"]
    return client, db[collection]