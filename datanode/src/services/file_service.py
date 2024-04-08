import config_pb2_grpc
import config_pb2
import os
import shutil
import grpc
from concurrent import futures

class FileService(config_pb2_grpc.FileServiceServicer):

    def getFile(self, request, context):
        # Buscar el archivo por su nombre y enviar los datos.
        file_path = os.path.join('file_chunks', request.file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                data = file.read()
            return config_pb2.GetFileResponse(file_name=request.file_name, data=data)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Archivo no encontrado')
            return config_pb2.GetFileResponse()

    def saveFile(self, request, context):
        print("Archivo en datanode")
        # Guardar el contenido del archivo.
        file_path = os.path.join('files', request.global_name, request.file_name)
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            file.write(request.content)
        return config_pb2.SaveFileResponse(status=True, file_name=request.file_name)

    def ReplicateFile(self, request, context):
        for file_part in request.file_parts:
            source_path = os.path.join(request.source_directory, file_part)
            target_path = os.path.join(request.target_directory, file_part)
            try:
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(source_path, target_path)
            except IOError as e:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details('Error durante la replicación: ' + str(e))
                return config_pb2.ReplicateFileResponse(success=False)
        return config_pb2.ReplicateFileResponse(success=True)