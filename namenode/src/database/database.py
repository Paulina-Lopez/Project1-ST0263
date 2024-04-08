# src/database/database.py

from pymongo import MongoClient
from bson import ObjectId

def connect(collection):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["DFS_DB"]
    return client, db[collection]

def get_files_from_failed_node(failed_node_id):
    _, files_collection = connect("files")
    # Encuentra los archivos asociados al nodo fallido
    files = files_collection.find({"node_id": ObjectId(failed_node_id)})
    return list(files)

def find_best_target_node(exclude_node_id):
    client, nodes_collection = connect("node")
    # Encuentra el nodo con el mayor espacio disponible excluyendo el nodo fallido
    best_node = nodes_collection.find_one(
        {"_id": {"$ne": ObjectId(exclude_node_id)}, "status": True},
        sort=[("capacity", -1)]
    )
    client.close()
    return best_node

def get_node_info(node_id):
    client, nodes_collection = connect("node")
    # Obtén la información del nodo dado un id
    node_info = nodes_collection.find_one({"_id": ObjectId(node_id)})
    client.close()
    return node_info
