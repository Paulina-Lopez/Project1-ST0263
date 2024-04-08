# replication_manager.py
from src.database.database import get_files_from_failed_node, find_best_target_node, connect
from services.config_pb2_grpc import FileServiceStub
from services.config_pb2 import ReplicateFileRequest
import grpc

def handle_replication(failed_node_id):
    client, collection = connect("node")
    files_to_replicate = get_files_from_failed_node(failed_node_id)
    target_node = find_best_target_node(exclude_node_id=failed_node_id, client=client)
    
    if target_node:
        channel = grpc.insecure_channel(f"{target_node['ip']}:{target_node['port']}")
        stub = FileServiceStub(channel)
        
        for file in files_to_replicate:
            replicate_request = ReplicateFileRequest(
                file_name=file['filename'],
                file_data=get_file_data(file['filename'])  # Necesitarás implementar esta función
            )
            try:
                response = stub.ReplicateFile(replicate_request)
                if not response.success:
                    print(f"Error replicando el archivo: {file['filename']}")
            except grpc.RpcError as e:
                print(f"Error gRPC al replicar archivo: {e}")

        channel.close()

    client.close()


#segunda opcion

# src/replication_manager.py
from database import connect, get_files_from_failed_node, find_best_target_node
from services.config_pb2_grpc import FileServiceStub
from services.config_pb2 import ReplicateFileRequest
import grpc

def handle_replication(failed_node_id):
    client, _ = connect(None)  # No necesitas el segundo valor de retorno aquí.
    files_to_replicate = get_files_from_failed_node(failed_node_id)
    target_node = find_best_target_node(exclude_node_id=failed_node_id)

    if target_node:
        # Inicia una conexión gRPC con el nodo de destino
        with grpc.insecure_channel(f"{target_node['ip']}:{target_node['port']}") as channel:
            stub = FileServiceStub(channel)
            
            # Itera a través de los archivos que se deben replicar
            for file_document in files_to_replicate:
                file_parts = [part['part_name'] for part in file_document['parts'] 
                              if part['node_id'] == failed_node_id]  # Asegúrate de que 'part_name' y 'node_id' son los campos correctos
                replicate_request = ReplicateFileRequest(
                    file_parts=file_parts,
                    source_directory="/ruta/a/los/archivos/existentes",  # Esta debe ser la ruta real de tus archivos
                    target_directory="/ruta/a/los/archivos/replicados"  # Esta es la ruta donde quieres replicar los archivos
                )

                # Envía la solicitud de replicación a través de gRPC
                try:
                    response = stub.ReplicateFile(replicate_request)
                    if not response.success:
                        print(f"Error replicando los archivos: {file_parts}")
                except grpc.RpcError as e:
                    print(f"Error de gRPC al intentar replicar los archivos: {e}")

    client.close()

def get_files_from_failed_node(failed_node_id):
    _, files_collection = connect("files")
    return list(files_collection.find({"parts.node_id": failed_node_id}))

def find_best_target_node(exclude_node_id):
    client, nodes_collection = connect("node")
    best_node = nodes_collection.find_one(
        {"_id": {"$ne": exclude_node_id}, "status": True},
        sort=[("capacity", -1)]
    )
    client.close()
    return best_node if best_node else None
