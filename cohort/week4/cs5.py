def get_details(name, key, lst):
    for entry in lst:
        if entry.get('name') != name:
            pass
        else:
            return entry.get(key)