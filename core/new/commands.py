import inspect
import os

from core.functions.system.getMainPath import *

commands = {
    " ": ""
}

key = "§§§§§"

def getCommands():
    global commands
    return commands


def update():
    comfile = open(getMainPath() + "core/plugins/PluginCommands.txt", "r+")

    coms = comfile.readlines()

    coms = "".join(coms)
    coms = coms.split(";")

    comsfinal = []

    for i in range(len(coms)):
        try:
            comsfinal = coms[i].split(":", 1)
            if comsfinal[1].startswith("\n"):
                comsfinal[1] = comsfinal[1].replace("\n", "")

            if comsfinal[0].startswith("\n"):
                comsfinal[0] = comsfinal[0].replace("\n", "")

            commands[comsfinal[0]] = comsfinal[1]

        except IndexError:
            pass

        comsfinal.clear()

    docbuiltins = os.listdir(getMainPath() + "core/functions/builtin")
    for i in range(len(docbuiltins)):
        exedoc = docbuiltins[i].replace(".py", "") + "." + docbuiltins[i].replace(".py", "")

        if docbuiltins[i] in ["__init__.py", "__pycache__"]:
            continue

        commands[docbuiltins[i].replace(".py", "")] = exedoc + "(args, self.instance.getInstance())"

    comfile.close()


def addCommand(command, code, pluginName, runable=False, needArgs=["args", "instance"]):
    """needArgs is only used, when code is a function"""
    comfile = open(getMainPath() + "core/plugins/PluginCommands.txt", "at")
    codefile = open(getMainPath() + "core/plugins/plugincodes.py", "at")
    # comfile = open("/Users/simonmennicken/Documents/GitHub/T2K/Doc/Doc/core/plugins/PluginCommands.txt", "at")

    if not runable:
        comfile.write(pluginName + " " + command.lower() + ":\"\"\"" + str(code) + "\"\"\";\n")

    else:
        try:
            code = code.split("\n")
            code = key.join(code)
            comfile.write(pluginName + " " + command.lower() + ":" + str(code) + ";\n")

        except:
            args = ""
            for i in range(len(needArgs)):
                args += needArgs[i]

            codepath = "plugins.plugincodes." + code.__code__.co_name + f"({args})"
            comfile.write(pluginName + " " + command.lower() + ":" + codepath + ";\n")

            source_code = inspect.getsource(code).split("\n", 1)[1]
            codefile.write(source_code)

    codefile.close()
    comfile.close()


def clear():
    comfile = open(getMainPath() + "/core/plugins/PluginCommands.txt", "w")
    codefile = open(getMainPath() + "core/plugins/plugincodes.py", "w")
    comfile.write("")
    codefile.write("")
    comfile.close()
