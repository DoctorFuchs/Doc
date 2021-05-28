import sys
import os
import time

sys.path.append(str(os.path.dirname(os.path.abspath(__file__))).replace("core", ""))

import version
from core.new import commands, debug, Listener, auth
from core.new.Interpret import interpreter


class doc:
    def __init__(self, username="USER", live_debug=False, guest=False, dev = False):
        start = time.time()

        self.debug = debug.debug(live_debug=live_debug)

        self.debug.addEvent("Starting DOC...", "SYSTEM")
        self.debug.addEvent("Clear Commands...", "SYSTEM")

        commands.clear()

        self.debug.addEvent("Clear Commands... Finished", "SYSTEM")
        self.debug.addEvent("Create Variables...", "SYSTEM")

        self.dev = dev

        # init names for debug
        self.username = username
        self.user = "USER:" + self.username
        self.plugin = "PLUGIN"
        self.consoleGeneral = "CONSOLE"
        self.system = "SYSTEM"
        self.consoleGeneral = "CONSOLE"
        self.consoleInput = "CONSOLE IN"
        self.consoleOutput = "CONSOLE OUT"

        self.installed = []

        self.instance = self

        self.debug.addEvent("Create Variables...Finished", self.system)
        self.debug.addEvent("Auth Build...", self.system)

        self.auth = auth.auth(self.instance)

        self.debug.addEvent("Auth Build... Finished", self.system)
        self.debug.addEvent("Listener Build...", self.system)

        self.Listener = Listener.Listener()
        self.Listener.subclass = False
        self.Listener.ConsoleStart()

        self.debug.addEvent("Listener Build... Finished", self.system)
        self.debug.addEvent("Interpret Build...", self.system)

        self.interpret = interpreter(instance=self.instance)

        self.debug.addEvent("Interpret Build... Finished", self.system)

        if __name__ == "system":
            self.sender = self.system

        else:
            self.sender = self.user

        self.debug.addEvent("Starting DOC... Finished", self.system)
        stop = time.time()

        start_time = round((stop - start) * 1000) / 1000

        if start_time < 1:
            start_time = "under 1"

        self.debug.addEvent("DOC started in " + str(start_time) + " second(s)", self.system)

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
        self.debug.addEvent(f"{command}", self.consoleInput)

        if command == "docinputevent":
            line_in = self.docinput(placeholder=f"[DOC][{self.username}]>>> ")

        else:
            line_in = command

        self.docprint(text=self.interpret.log(line_in), consoleOutput=True)

    def docprint(self, text, consoleOutput=False, end="\n"):
        text = str(text)
        self.Listener.Print(text=text)
        if consoleOutput:
            self.debug.addEvent("Output: " + text, self.consoleOutput)

        if text == "None":
            pass

        else:
            print(text, end=end)

    def docinput(self, placeholder="") -> str:
        # input
        userinput = input(placeholder + "")
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
                    self.debug.addEvent("Console Exited", self.consoleGeneral)
                    break

        except Exception as e:
            if not self.dev:
                self.docprint("Exit console")
                self.Listener.TerminalClientStop()
                self.debug.addEvent("Console Exited", self.consoleGeneral)
                quit()

            else:
                raise e

    def getInstance(self):
        return self.instance

    def installPackage(self, packageName: str):
        path = f"plugins/{packageName}"
        self.Listener.PluginInstall(packageName, path)
        self.debug.addEvent("Install Package " + packageName + " from " + path, self.plugin)
        exec(f"import core.plugins.{packageName}.DOC as {packageName}")


if __name__ == '__main__':
    this = doc(guest=False, username="Hallo", dev=True)
    this.terminalclient()

