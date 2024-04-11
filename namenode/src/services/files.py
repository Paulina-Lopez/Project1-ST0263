from src.database.database import connect
from datetime import datetime
import json

def add_file(body):
    client, collection = connect("files")
    client1, collection1 = connect("node")

    response = { "message": "Unexpected error", "status": False }

    try:

        on_nodes = collection1.find({"status": True}).limit(4)
        on_nodes_list = list(on_nodes)
        f_racks, f_parts = generate_save_rule(body['total_parts'], on_nodes_list, body['parts'])
        file = {
            "filename": body["file_name"],
            "file_extension": body["file_extension"],
            "total_parts": body["total_parts"],
            "racks": f_racks,
            "parts": f_parts,
            "created_date": str(datetime.now())
        }

        inserted_file = collection.insert_one(file)
        inserted_id = inserted_file.inserted_id
        inserted_document = collection.find_one({"_id": inserted_id})
        inserted_document["_id"] = str(inserted_document["_id"])

        listnode = []
        for n in on_nodes_list:
            listnode.append(
                {
                    "_id": str(n["_id"]),
                    "name": n["name"],
                    "ip": n["ip"],
                    "port": n["port"]
                }
            )
        response = { "message": "Correct add file", "status": True, "data_file": inserted_document, "data_node": listnode}
    except Exception as e:
        print(e)
        response = { "message": e, "status": False } 
    client.close()
    client1.close()
    print(response)
    return response

def generate_save_rule(parts, nodes, prev_parts):
    final_parts = []
    total_rack = []
    try:
        count = 0
        grup1 = parts // 2
        grup2 = parts - grup1
        total_nodes = len(nodes)

        if total_nodes >= 2 and total_nodes <= 3:
            total_rack.append({
                "rack_name": "rack_1",
                "nodes": [str(nodes[0]["_id"])]
            })
            total_rack.append({
                "rack_name": "rack_2",
                "nodes": [str(nodes[1]["_id"])]
            })
            while count < parts:
                for pp in prev_parts:
                    if count < grup1:
                        final_parts.append({
                            "file_name": pp,
                            "node": str(nodes[0]["_id"])
                        })
                    else:
                        final_parts.append({
                            "file_name": pp,
                            "node": str(nodes[1]["_id"])
                        })
                    count += 1
        if total_nodes >= 4:
            total_rack.append({
                "rack_name": "rack_1",
                "nodes": [str(nodes[0]["_id"]), str(nodes[2]["_id"])]
            })
            total_rack.append({
                "rack_name": "rack_2",
                "nodes": [str(nodes[1]["_id"]), str(nodes[3]["_id"])]
            })
            while count < parts:
                for pp in prev_parts:
                    if count < grup1:
                        final_parts.append({
                            "file_name": pp,
                            "node": str(nodes[0]["_id"])
                        })
                        final_parts.append({
                            "file_name": pp,
                            "node": str(nodes[2]["_id"])
                        })
                    else:
                        final_parts.append({
                            "file_name": pp,
                            "node": str(nodes[1]["_id"])
                        })
                        final_parts.append({
                            "file_name": pp,
                            "node": str(nodes[3]["_id"])
                        })
                    count += 1
    except Exception as e:
        print(e)
    return total_rack, final_parts


def search_files(file_name):
    client, collection = connect("files")
    try:
        results = collection.find({"filename": {"$regex": file_name, "$options": "i"}}, {"filename": 1, "file_extension": 1})
        files = [{"name": result["filename"], "extension": result["file_extension"]} for result in results]
        return files
    except Exception as e:
        print(e)
        return []
    finally:
        client.close()

def update_file(file_name, parts):
    client, collection = connect("files")
    response = { "message": "Node not found", "status": False }
    query = { "filename": file_name }
    try:
        collection.find_one_and_update(query, { "$set": { "parts": parts}})
    except Exception as e:
        response = { "message": e, "status": False } 

    client.close()
    return response
