import sys
import os
import time

sys.path.append(str(os.path.dirname(os.path.abspath(__file__))).replace("core", ""))

import version
from core.new import commands, debug, Listener, auth
from core.new.Interpret import interpreter
from core.functions.system.Sections import *


class doc:
    def __init__(self, username="USER", live_debug=False, guest=False, dev=False):
        start = time.time()

        self.debug = debug.debug(instance=self, live_debug=live_debug)

        self.debug.addEvent("Listener Build...", SYSTEM)

        self.Listener = Listener.Listener()
        self.Listener.subclass = False
        self.Listener.ConsoleStart()

        self.debug.addEvent("Listener Build... Finished", SYSTEM)
        self.debug.start = True

        self.debug.addEvent("Starting DOC...", SYSTEM)
        self.debug.addEvent("Clear Commands...", SYSTEM)

        commands.clear()

        self.debug.addEvent("Clear Commands... Finished", SYSTEM)
        self.debug.addEvent("Create Variables...", SYSTEM)

        self.dev = dev

        # init names for debug
        self.username = username
        self.user = "USER:" + self.username
        self.sender = self.user

        self.installed = []

        self.instance = self

        self.debug.addEvent("Create Variables...Finished", SYSTEM)
        self.debug.addEvent("Auth Build...", SYSTEM)

        self.auth = auth.auth(self.instance)

        self.debug.addEvent("Auth Build... Finished", SYSTEM)
        self.debug.addEvent("Interpret Build...", SYSTEM)

        self.interpret = interpreter(instance=self.instance)

        self.debug.addEvent("Interpret Build... Finished", SYSTEM)
        self.debug.addEvent("Starting DOC... Finished", SYSTEM)
        stop = time.time()

        start_time = round((stop - start) * 1000) / 1000

        if start_time < 1:
            start_time = "under 1"

        self.debug.addEvent("DOC started in " + str(start_time) + " second(s)\n", SYSTEM)
        self.debug.start = False

        if not guest:
            try:
                self.auth.login()

            except:
                self.docprint("login failed! exit")
                self.Listener.ConsoleExit(400)
                quit()

        else:
            self.username = "USER"

    def log(self, command="docinputevent"):
        self.interpret.update()
        self.Listener.ConsoleRun(command=command, sender=self.sender)
        self.debug.addEvent(f"{command}", CONSOLE_IN)

        if command == "docinputevent":
            line_in = self.docinput(placeholder=f"[DOC][{self.username}]>>> ")

        else:
            line_in = command

        self.docprint(text=self.interpret.log(line_in))

    def docprint(self, text, end="\n", display_section=OUTPUT, debug_it=True):
        text = str(text)
        if debug_it:
            self.Listener.Print(text=text)
            self.debug.addEvent("Docprint: " + text, str(display_section))

        if text == "None":
            pass

        else:
            sys.stdout.write(text+end)
            sys.stdout.flush()

    def docinput(self, placeholder="", debug_it=True) -> str:
        # input
        self.docprint(placeholder, end="")
        userinput = sys.stdin.readline().replace("\n", "")

        if debug_it:
            self.debug.addEvent("Docinput: "+userinput, source=INPUT)
            self.Listener.UserInput(self.username, userinput)

        return userinput

    def terminalclient(self):
        self.Listener.TerminalClientStart()
        self.docprint("DOC-TERMINAL_CLIENT running DOC-" + version.version)
        try:
            while True:
                line_in = self.docinput(placeholder=f"[DOC][{self.username}]>>> ")
                if line_in.lower() != "exit":
                    self.docprint(self.log(line_in.lower()))
                    continue

                else:
                    self.Listener.TerminalClientStop(exitCode=200)
                    self.debug.addEvent("Console Exited", CONSOLE)
                    break

        except Exception as e:
            if not self.dev:
                self.docprint("Exit console")
                self.Listener.TerminalClientStop()
                self.debug.addEvent("Console Exited", CONSOLE)
                quit()

            else:
                raise e

    def getInstance(self):
        return self.instance

    def installPackage(self, packageName: str):
        path = f"plugins/{packageName}"
        self.Listener.PluginInstall(packageName, path)
        self.debug.addEvent("Install Package " + packageName + " from " + path, PLUGIN)
        exec(f"import core.plugins.{packageName}.DOC as {packageName}")


if __name__ == '__main__':
    this = doc(guest=False, username="Hallo", dev=True)
    this.terminalclient()
