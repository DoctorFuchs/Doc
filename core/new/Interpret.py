import sys

from core.functions.system.getMainPath import getMainPath
from core.new import commands
from core import plugins
from core.plugins import plugincodes
import importlib as imp
import os

for i in range(len(os.listdir(getMainPath() + "core/functions/builtin"))):
    if os.listdir(getMainPath() + "core/functions/builtin")[i].endswith(".py"):
        exec("from core.functions.builtin import " + os.listdir(getMainPath() + "core/functions/builtin")[i].replace(
            ".py", ""))


class Event:
    def __init__(self, instance, args: dict, builtin = False):
        self.args = args
        self.print = instance.docprint
        self.input = instance.docinput
        self.__installPackage__ = instance.installPackage
        self.installed = instance.installed
        if builtin:
            self.Listener = instance.Listener
            self.Debug = instance.debug


class interpreter:
    def __init__(self, instance):
        self.commands = commands.getCommands()
        self.instance = instance

    def update(self):
        imp.reload(plugincodes)
        self.commands = commands.getCommands()

    def log(self, command):
        self.instance.debug.addEvent(event="Update Plugin Commands", source="PLUGINLOG")
        self.instance.Listener.commandUpdate(self)
        commands.update()

        com = ""
        try:
            c = command.split()

            com = c[0].lower()

            del (c[0])
            args = c

        except:
            args = []

        builtin = com+".py" in os.listdir(getMainPath()+"core/functions/builtin")
        event = Event(self.instance, args, builtin)

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
                for j in range(len(obj)):
                    eval(obj[j])

            except (KeyError, IndexError) as e:
                try:
                    self.instance.docprint(f"{com} has no command " + args[0])

                except:
                    try:
                        obj = self.commands[com + " "]
                        eval(obj)

                    except:
                        self.instance.docprint(f"{com} is an installed Plugin")

            except Exception as e:
                if self.instance.dev:
                    raise e

                else:
                    self.instance.docprint(
                        f"The {com} plugin raise an error! \nContact the developer with open an issue"
                        f"on Github")

        else:
            return "no command named " + com

    def logfile(self, path):
        try:
            file = open(path, "r")

        except FileNotFoundError:
            self.instance.docprint("File not found")
            return

        for command in file.readlines():
            self.instance.docprint(self.log(command))
