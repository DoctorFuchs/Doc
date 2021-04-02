commands = {
    "echo": "echo(args)",
    "pack": "pack(args, this)",
    "commands": "commands.getCommands()",
    " ": ""
}

key = "§§§§§"


def getCommands():
    global commands
    return commands


def getMainPath():
    path = str(__file__).split("/")
    del path[len(path) - 1]
    return "/".join(path) + "/"


def update():
    comfile = open(getMainPath() + "plugins/PluginCommands.txt", "r+")

    coms = comfile.readlines()

    coms = "".join(coms)
    coms = coms.split(";")

    comsfinal = []

    for i in range(len(coms)):
        try:
            comsfinal = coms[i].split(":", 1)
            if comsfinal[1].startswith("\n"):
                comsfinal[1] = comsfinal[1].replace("\n", "")

            commands[comsfinal[0]] = comsfinal[1]

        except IndexError:
            pass

        comsfinal.clear()

    comfile.close()


def addCommand(command, code, pluginName, runable=False):
    comfile = open(getMainPath() + "plugins/PluginCommands.txt", "at")

    if not runable:
        comfile.write(pluginName + " " + command + ":\"\"\"" + str(code) + "\"\"\";\n")

    else:
        code = code.split("\n")
        code = key.join(code)
        comfile.write(pluginName + " " + command + ":" + str(code) + ";\n")

    comfile.close()


def clear():
    comfile = open(getMainPath() + "plugins/PluginCommands.txt", "w")
    comfile.write("")
    comfile.close()