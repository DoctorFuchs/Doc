import os
import shutil

from core.functions.system.getMainPath import getMainPath

try:
    from version import *

except:
    version = "1.1.4"

try:
    import requests as req
    import torpy as tor
    from torpy.http import requests
    from torpy.http.adapter import TorHttpAdapter

except:
    print("request or torpy is not installed. (install both with pip3) Please update manually")

blocked = ["core/new/auths.py", "core/plugins", "core/startup.txt"]  # files, that don't get update


def getPath():
    path = str(__file__).split("core/functions/system/updater.py")
    del path[len(path) - 1]

    path = "/".join(path).split("/")
    path.append("Doc-" + getGithubVersion())

    del path[len(path) - 3]
    if not os.path.isdir("/".join(path)):
        os.mkdir("/".join(path))

    return ("/".join(path) + "/").replace("//", "/")


def getGithubVersion(session=None) -> str:
    if session is None:
        raw = req.get("https://raw.githubusercontent.com/DoctorFuchs/Doc/main/version.py")  # request raw document

    else:
        raw = session.get("https://raw.githubusercontent.com/DoctorFuchs/Doc/main/version.py")

    if raw.status_code != 200:  # if user is not online
        return version

    return raw.text.split("version = ")[1].split("<")[0].replace("\"", "").replace("\n", "")


def getContent(path: str, session=None) -> str:
    if session is None:
        raw = req.get("https://raw.githubusercontent.com/DoctorFuchs/Doc/main/" + path)  # request raw document

    else:
        raw = session.get("https://raw.githubusercontent.com/DoctorFuchs/Doc/main/" + path)

    if raw.status_code != 200:  # if user is not online
        return ""

    return raw.text


def getAllFilesInDictionary(path: str, github="doctorfuchs/doc", session=None):
    if session is None:
        info = req.get(f"https://api.github.com/repos/{github}/contents/" + path)

    else:
        info = session.get(f"https://api.github.com/repos/{github}/contents/" + path)

    if info.status_code != 200:
        return []

    file = {}
    returner = []
    final = info.text.split(">")[0].split("</pre>")[0].replace("{", ",").replace("}", ",").replace("\"", "").split(",")

    # convert to dict
    for i in range(len(final)):
        if final[i] == "":
            pass

        if final[i].split(":", 1)[0] == "name" and file != {}:
            file[final[i].split(":", 1)[0]] = final[i].split(":", 1)[1]
            returner.append(file)
            file = {}

        else:
            try:
                file[final[i].split(":", 1)[0]] = final[i].split(":", 1)[1]

            except IndexError:
                pass

    returner.append(file)

    return returner


def update(sess=None, github="DoctorFuchs/Doc"):
    file_paths = []
    dicts = ["", ""]

    while True:
        try:
            act = getAllFilesInDictionary(dicts[0], session=sess, github=github)
            for i in range(len(act)):
                if act[i]["path"] in blocked:
                    continue

                if act[i]["type"] == "file":
                    file_paths.append(act[i]["path"])

                elif act[i]["type"] == "dir":
                    try:
                        os.mkdir(getPath() + act[i]["path"])

                    except FileExistsError:
                        pass

                    dicts.append(act[i]["path"])

            del dicts[0]

        except:
            break

    for element in range(len(file_paths)):
        content = getContent(file_paths[element], session=sess)

        if file_paths[element] in blocked:
            continue

        elif os.path.isfile(getPath() + file_paths[element]):
            mode = "r+t"

        else:
            mode = "w+t"

        file = open(getPath() + file_paths[element], mode)
        if "\n".join(file.readlines()) == content:
            pass

        else:
            file.writelines(content.split("\n"))

        file.close()

    for i in range(len(blocked)):
        try:
            shutil.copy(getMainPath() + blocked[i], getPath() + blocked[i])

        except IsADirectoryError:
            try:
                shutil.copytree(getMainPath() + blocked[i], getPath() + blocked[i])

            except:
                pass

        except FileNotFoundError:
            pass

    return "updated"


def tor_update(github="Doctorfuchs/Doc"):
    with tor.TorClient() as torc:
        with torc.get_guard() as guard:
            adapter = TorHttpAdapter(guard, 2)
            with requests.Session() as sess:
                sess.headers.update({"User-Agent": "Mozilla/5.0"})
                sess.mount("https://", adapter)
                update(sess, github)
