from src.database.database import connect
from datetime import datetime


def node_alive (ip, port):
    client, collection = connect("node")
    response = { "message": "Node no reported", "status": False }
    try:
        now = datetime.now()
        collection.find_one_and_update({ "ip": ip, "port": port }, { '$set': { "report_date": now, "status": True }})
        response = { "message": "Node report success", "status": True }
    except Exception as e:
        response = { "message": e, "status": True }
    client.close()
    return response

def create_node (name, ip, port):
    client, collection = connect("node")
    response = { "message": "Error no created", "status": False }
    node = {
        "name": name,
        "ip": ip, 
        "port": port,
        "capacity": 10,
        "report_date": datetime.now(),
        "status": True
    }
    
    try:
        collection.insert_one(node)
        response = { "message": "Node created", "status": True }
    except Exception as e:
        response = { "message": e, "status": False }
    client.close()
    return response
    