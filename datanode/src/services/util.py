

def split_file():
    chunk_size = 1024
    input_file = "/files/{name}"
    parts = []
    with open(input_file, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            parts.append(chunk)
            part_num += 1
    return parts

def join_file():
    pass