import grpc
import os
from concurrent import futures
from server_pb2 import GetFile, FileResult, Parts, SaveFileRequest, SaveFileResponse
from server_pb2_grpc import FileServiceServicer, add_FileServiceServicer_to_server

class FileService(FileServiceServicer):
    def getFile(self, request, context):
        file_name = request.file_name
        file_path = os.path.join("files", file_name)

        if not os.path.exists(file_path):
            context.set_details(f"El archivo '{file_name}' no existe.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return FileResult()

        with open(file_path, "rb") as file:
            file_content = file.read()
        partes_del_archivo = [file_content]

        file_result = FileResult()
        file_result.file_name = file_name
        file_result.total_parts = len(partes_del_archivo)
        for parte in partes_del_archivo:
            file_result.parts.append(Parts(data=parte))
        return file_result
    
    def saveFile(self, request, context):
        file_name = request.file_name
        content = request.content
        file_path = os.path.join("files", file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            file.write(content)
        
        return SaveFileResponse(status=True, file_name=file_name)

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    pass

if __name__ == "__main__":
    server()