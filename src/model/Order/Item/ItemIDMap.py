item_id_map = None


def generateIdMap(items: list):
    global item_id_map
    item_id_map = {}
    for item in items:
        item_id_map[int(item['additional_data'])] = item['item_id']


def getIdMap():
    return item_id_map
