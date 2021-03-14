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

    comsfinal = []

    for i in range(len(coms)):
        comsfinal = coms[i].split(":", 1)
        commands[comsfinal[0]] = comsfinal[1]
        comsfinal.clear()

    comfile.close()


def addCommand(command, code):
    comfile = open("plugins/PluginCommands.txt", "at")

    comfile.write(command + ":" + code + "\n")

    comfile.close()

