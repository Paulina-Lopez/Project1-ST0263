from bson import ObjectId
from src.database.database import connect
from datetime import datetime
from random import choice
import grpc
import sys
# sys.path.append('C:/Users/PaulinaLopezSalazar/Documents/Universidad/p2p2/namenode/src')
from config_pb2 import ReplicateFileRequest
from config_pb2_grpc import FileServiceStub


def node_alive (ip, port):

    print(ip, port)    
    client, collection = connect("node")
    response = { "message": "Node no reported", "status": False }
    try:
        now = datetime.now()
        print(f"reporta {ip}:{port}-{now}")
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


def choose_active_node():
    client, collection = connect("node")
    try:
        query = {"status": True}
        active_nodes = list(collection.find(query))
        if not active_nodes:
            raise Exception("No active nodes found")
        selected_node = choice(active_nodes)
        return selected_node
    except Exception as e:
        print(f"Error choosing active node: {e}")
        return None
    finally:
        client.close()


def get_files_from_node(node_id):
    client, collection = connect("files")
    try:
        query = {"parts.node": node_id}
        files = list(collection.find(query))
        file_list = [{
            'filename': file['filename'],
            'file_extension': file['file_extension'],
            'total_parts': file['total_parts'],
            'created_date': file['created_date'],
            'parts': file['parts'],
            'racks': file['racks']
        } for file in files]
        return file_list
    except Exception as e:
        print(f"Error {node_id}: {e}")
        return []
    finally:
        client.close()


def update_file_locations(file, new_node_id, parts):
    client, collection = connect("files")
    part_list = []
    try:

        for p in parts:
            part_list.append({
                "file_name": p,
                "node": new_node_id
            })
        collection.find_one_and_update({"_id": file["_id"]},
                                       { '$set': { 'parts': part_list }})
    except Exception as e:
        print(f"Error updating file locations: {e}")
    finally:
        client.close()


def replicate_file(file, new_node_id, bck_node, bck_files):
    try:
        with grpc.insecure_channel(f'{new_node_id["ip"]}:{new_node_id["port"]}') as channel:
            stub = FileServiceStub(channel)
            request = ReplicateFileRequest(
                file=str(file),
                file_parts=bck_files,
                backup_node=bck_node,
            )

            response = stub.ReplicateFile(request)
            handle_file_response(response, file, new_node_id)
            channel.close()
    except grpc.RpcError as e:
        print(f"gRPC error occurred: {e}")


def handle_file_response(response, file, new_node_id):
    if response.success:
        print(f"File {file['filename']} replicated successfully to node {new_node_id["ip"]}.")
    else:
        print(f"Failed to replicate file {file['filename']} to node {new_node_id["ip"]}.")