from core.functions.system.getMainPath import getMainPath
from core.new import commands
from core import plugins
from core.plugins import plugincodes
import importlib as imp
import os

for i in range(len(os.listdir(getMainPath() + "core/functions/builtin"))):
    exec("from core.functions.builtin import " + os.listdir(getMainPath() + "core/functions/builtin")[i].replace(".py",
                                                                                                                 ""))


class interpreter:
    def __init__(self, instance):
        self.commands = commands.getCommands()
        self.instance = instance

    def update(self):
        imp.reload(plugincodes)
        self.commands = commands.getCommands()

    def log(self, command):
        self.instance.debug.addEvent(event="Update Plugin Commands", source="PLUGINLOG")
        self.instance.Listener.commandUpdate()
        commands.update()

        com = ""
        try:
            c = command.split()

            com = c[0].lower()

            del (c[0])
            args = c

        except:
            pass

        if com in " ":
            pass

        elif com in self.commands:
            object = self.commands[com]
            return eval(object)

        elif com in self.instance.installed:
            try:
                object = self.commands[com + " " + args[0]]
                obj = []

                obj = object.split(commands.key)
                for i in range(len(obj)):
                    instance = self.instance
                    eval(obj[i])

            except KeyError:
                try:
                    self.instance.docprint(f"{com} has no command " + args[0])

                except:
                    self.instance.docprint(f"{com} is an installed Plugin")

        else:
            return "no command named " + com