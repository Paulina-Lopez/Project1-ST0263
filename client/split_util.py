import os

def get_filename_and_extension(file_name):
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    extension = os.path.splitext(file_name)[1]
    return base_name, extension

def split_into_files(input_file, output_directory, chunk_size):
    os.makedirs(output_directory, exist_ok=True)
    file_name, file_extension = get_filename_and_extension(input_file)

    parts = []
    with open(input_file, 'rb') as file:
        chunk_number = 0
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            output_file = os.path.join(output_directory, f'part_{chunk_number}.bin')
            parts.append(f'part_{chunk_number}.bin')
            with open(output_file, 'wb') as outfile:
                outfile.write(chunk)

            chunk_number += 1

    document = {
        "file_name": file_name,
        "file_extension": file_extension,
        "directory": output_directory,
        "total_parts": chunk_number,
        "parts": parts
    }
    return document
