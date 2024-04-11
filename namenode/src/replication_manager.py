from .services.node import choose_active_node, get_files_from_node, update_file_locations, replicate_file
from src.database.database import connect

def handle_replication(node_id):
    client, collection = connect("node")
    files = get_files_from_node(node_id)

    new_node_id = choose_active_node()
    if not new_node_id or not files:

        return
    for file in files:
        bck_node = obtener_otro_id_en_mismo_rack(node_id, file["racks"])
        partes_bck = obtener_partes_por_id(bck_node, file)


        bck_node_info = collection.find_one({"_id": bck_node})
        # cont = {
        #     "file": file,
        #     "new_node_id": str(new_node_id["_id"]),
        #     "bck_node": bck_node_info,
        #     "partes_bck": partes_bck
        # }

        replicate_file(file, new_node_id, bck_node_info, partes_bck)
        update_file_locations(files, new_node_id, partes_bck)
    client.close()



def obtener_otro_id_en_mismo_rack(id_a_buscar, racks):
    a = buscar_id_en_racks(id_a_buscar, racks)
    print(a)
    for rack in racks:
        if rack["rack_name"] == a:
            for n in rack["nodes"]:
                if n != id_a_buscar:
                    return n
    


def buscar_id_en_racks(id_a_buscar, racks):
    for rack in racks:
        if id_a_buscar in rack["nodes"]:
            return rack["rack_name"]
    return None

def obtener_partes_por_id(id_a_buscar, data):
    partes = []
    for parte in data["parts"]:
        if parte["node"] == id_a_buscar:
            partes.append(parte["file_name"])
    return partes

def obtener_otro_id_en_misma_posicion(id_a_buscar, racks):

    a, b = buscar_id_en_racks(id_a_buscar, racks)
    for r in racks:
        if r["rack_name"] == a:
            return r["nodes"][b]


    # rack_encontrado, posicion = buscar_id_en_racks(id_a_buscar, racks)
    # if rack_encontrado is not None and posicion is not None:
    #     otro_rack = racks[1] if rack_encontrado == racks[0]["rack_name"] else racks[0]
    #     otro_id = otro_rack["nodes"][posicion]
    #     return otro_id
    # return None