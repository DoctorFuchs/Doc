import os
from builtins import IndexError

import requests

from core.functions.system.getMainPath import getMainPath

blocked = []


def getContent(pluginname: str, path: str, session=None) -> str:
    if session is None:
        raw = requests.get(
            "https://raw.githubusercontent.com/doc-client/" + pluginname + "/main/" + path)  # request raw document

    else:
        raw = session.get("https://raw.githubusercontent.com/doc-client/" + pluginname + "/main/" + path)

    if raw.status_code != 200:  # if user is not online
        return ""

    return raw.text


def getAllFilesInPlugin(pluginname, sess=None) -> list:
    if sess is None:
        info = requests.get("https://api.github.com/repos/Doc-client/" + pluginname + "/contents/")

    else:
        info = sess.get("https://api.github.com/repos/Doc-client/" + pluginname + "/contents/")

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


def getPath(pluginname):
    if pluginname != "":
        return getMainPath() + "core/plugins/"+pluginname+"/"

    else:
        return getMainPath() + "core/plugins/"


def getAvailablePlugins():
    info = requests.get("https://api.github.com/users/Doc-client/repos")

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


def download(pluginname):
    avai = getAvailablePlugins()
    for i in range(len(avai)):
        try:
            if pluginname in getAvailablePlugins()[i]["name"]:
                break

        except:
            pass

        if i == len(avai)-1:
            return "not an available plugin for Doc"

    file_paths = []
    dicts = ["", ""]

    while True:
        try:
            act = getAllFilesInPlugin(pluginname)
            for i in range(len(act)):
                if act[i]["path"] in blocked:
                    continue

                if act[i]["type"] == "file":
                    file_paths.append(act[i]["path"])

                elif act[i]["type"] == "dir":
                    try:
                        os.mkdir(getPath(pluginname) + act[i]["path"])

                    except FileExistsError:
                        pass

                    dicts.append(act[i]["path"])

            del dicts[0]

        except IndexError:
            break

    os.mkdir(getPath(pluginname))

    for element in range(len(file_paths)):
        content = getContent(pluginname, file_paths[element])
        if file_paths[element] in blocked:
            continue

        elif os.path.isfile(getPath(pluginname) + file_paths[element]):
            mode = "r+t"

        else:
            mode = "w+t"

        file = open(getPath(pluginname) + file_paths[element], mode)

        file.write(content)

        file.close()

    return "successful installed"


def store(args, instance):
    """install plugins from github"""
    try:
        if args[0] == "install":
            if args[1] not in os.listdir(getPath("")):
                instance.docprint(download(args[1]))

            else:
                instance.docprint("already installed")

            return

        elif args[0] == "list":
            instance.docprint("Available plugins:")
            avai = getAvailablePlugins()

            for i in range(len(avai)):
                try:
                    if avai[i]["name"] in os.listdir(getPath("")):
                        installed = " - already installed"

                    else:
                        installed = " - not installed"

                    instance.docprint("\t"+avai[i]["name"] + ": " + avai[i+1]["description"] + installed)

                except KeyError:
                    pass

                i += 1

            instance.docprint("")
            return

    except IndexError:
        pass

    instance.docprint("""
usage:  
    install <plugin>
    list
""")
