def itemsSort(items):
    hash_map = {}
    for i, item in enumerate(items):
        hash_map[item[i]] = 1 + hash_map.get(items[i], 0)
        