def get_keys(dictt: dict):
    keys = str(dictt.keys())
    keys = "".join(keys.split("dict_keys(["))
    keys = "".join(keys.split("])"))
    keys = keys.split(", ")

    for k in range(len(keys)):
        try:
            keys[k] = keys[k].split("'")[1]

        except:
            pass

    return keys
