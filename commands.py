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


def update():
    comfile = open("plugins/PluginCommands.txt", "r+")

    coms = comfile.readlines()

    coms = "".join(coms)
    coms = coms.split(";")

    comsfinal = []

    for i in range(len(coms)):
        try:
            comsfinal = coms[i].split(":", 1)
            commands[comsfinal[0]] = comsfinal[1]

        except IndexError:
            pass

        comsfinal.clear()

    comfile.close()


def addCommand(command, code, pluginName, runable=False):
    comfile = open("plugins/PluginCommands.txt", "at")

    if not runable:
        comfile.write(pluginName+" "+command + ":\"\"\"" + str(code) + "\"\"\";\n")

    else:
        code = code.split("\n")
        code = key.join(code)
        comfile.write(pluginName+" "+command + ":" +str(code) + ";\n")

    comfile.close()