import os

def join_files(file_id, output_folder, chunks_folder='file_chunks'):
    specific_chunks_folder = os.path.join(chunks_folder, file_id)
    file_chunks = os.listdir(specific_chunks_folder)
    file_chunks.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    output_file_path = os.path.join(output_folder, file_id)
    with open(output_file_path, 'wb') as output_file:
        for chunk_name in file_chunks:
            chunk_path = os.path.join(specific_chunks_folder, chunk_name)
            with open(chunk_path, 'rb') as file_chunk:
                output_file.write(file_chunk.read())
    return output_file_path
