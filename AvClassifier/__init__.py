def avClassifier(av_path):
    returner = {}
    value = ""
    key = None
    print(value)

    with open(av_path, 'rb') as patterns:
        patern = patterns.readlines()

    for index, menus in enumerate(patern, 1):
        if menus.find(b':') and not key and value == "":
            num = menus.find(b':')
            key = menus.decode('ascii')[:num].strip()
            value += menus.decode('ascii')[num + 1:].strip()
        else:
            value += menus.decode('ascii').strip()
        if menus == b'\r\n' or index == len(patern):
            if value and key:
                returner[key] = eval(value)
                value, key = "", None
            continue
    return returner