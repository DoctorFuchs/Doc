commands = {
    "echo": "echo(args)",
    "pack": "pack(args, this)",
    "commands": "commands.getCommands()",
    " ": ""
}


def getCommands():
    global commands
    return commands


def update():
    comfile = open("plugins/PluginCommands.txt", "r+")

    coms = comfile.readlines()
    print(coms)

    comsfinal = []

    for i in range(len(coms)):
        comsfinal = coms[i].split(":", 1)
        commands[comsfinal[0]] = comsfinal[1]
        comsfinal.clear()

    comfile.close()


def addCommand(command, code, pluginName, runable=False):
    comfile = open("plugins/PluginCommands.txt", "at")

    if not runable:
        comfile.write(pluginName+" "+command + ":\"" + str(code) + "\"\n")

    else:
        comfile.write(pluginName+" "+command + ":" + str(code) + "\n")

    comfile.close()