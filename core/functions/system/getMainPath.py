def getMainPath():
    path = str(__file__).split("/core/functions/system/getMainPath.py")
    del path[len(path)-1]
    return "/".join(path) + "/"
