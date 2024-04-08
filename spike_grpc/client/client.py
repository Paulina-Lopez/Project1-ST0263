import grpc
import os
from server_pb2 import GetFile
from server_pb2_grpc import FileServiceStub

def main():
    # Establece la conexión al servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = FileServiceStub(channel)
        request = GetFile(file_name="test.txt")
        response = stub.getFile(request)
        handle_file_response(response)

def handle_file_response(response):
    directorio_destino = "files/"
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    
    ruta_archivo_local = os.path.join(directorio_destino, "test.txt")

    with open(ruta_archivo_local, "wb") as archivo:
        for parte in response.parts:
            archivo.write(parte.data)

    print(f"Archivo guardado en: {ruta_archivo_local}")

if __name__ == '__main__':
    main()