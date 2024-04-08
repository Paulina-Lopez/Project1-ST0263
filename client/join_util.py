from pymongo import MongoClient
import os


MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["DFS_DB"]
coleccion = db["files"]


def join_files(file_name, output_directory):
    base_nombre = file_name.split('.')[0]
    documento = coleccion.find_one({"filename": base_nombre})
    if documento is None:
        raise ValueError(f"No se encontró información en MongoDB para el archivo {base_nombre}")
    file_extension = documento.get("file_extension", "")
    input_directory = os.path.join(base_nombre)
    output_file_path = os.path.join(output_directory, base_nombre + file_extension)
    os.makedirs(output_directory, exist_ok=True)
    with open(output_file_path, 'wb') as output_file:
        chunk_number = 0
        while True:
            input_file = f'{base_nombre}_chunk{chunk_number}{file_extension}'
            input_file_path = os.path.join(input_directory, input_file)
            if not os.path.exists(input_file_path):
                break
            with open(input_file_path, 'rb') as input_chunk:
                output_file.write(input_chunk.read())

            chunk_number += 1
    return output_file_path
