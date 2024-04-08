import os
import grpc
import json
from config_pb2_grpc import FileServiceStub
from config_pb2 import SaveFileRequest, SaveFileResponse

def handle_file_response(response, part_full_name):
    if isinstance(response, SaveFileResponse) and not response.status:
        raise Exception(f"Failed to save file {part_full_name} on datanode.")

def send_grpc(file_info, nodes):
    file_full_name = f"{file_info['filename']}{file_info['file_extension']}"
    for part in file_info['parts']:
        part_full_name = os.path.join('file_chunks', file_full_name, part['file_name'])
        with open(part_full_name, 'rb') as file:
            file_content = file.read()

        node = next((node for node in nodes if node['_id'] == part['node']), None)
        if node:
            with grpc.insecure_channel(f"{node['ip']}:{node['port']}") as channel:
                stub = FileServiceStub(channel) 
                request = SaveFileRequest(global_name=file_full_name, file_name=part['file_name'], content=file_content)
                response = stub.saveFile(request)
                handle_file_response(response, part_full_name)
