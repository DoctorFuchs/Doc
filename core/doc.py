import getpass
import sys
import os
import time

sys.path.append(str(os.path.dirname(os.path.abspath(__file__))).replace("core", ""))

import version
from core.new import commands, debug, Listener, auth
from core.new.Interpret import interpreter
from core.functions.system.Sections import *
from core.functions.system import updater


class doc:
    def __init__(self, username="USER", live_debug=False, guest=False, dev=False):
        start = time.time()

        self.debug = debug.debug(instance=self, live_debug=live_debug)
        self.debug.start = True

        self.debug.addEvent("Starting DOC...", SYSTEM)

        self.debug.addEvent("Checking for updates...", SYSTEM)

        new_version = updater.getGithubVersion()

        if new_version == version.version:
            self.debug.addEvent("No updates found", SYSTEM)

        else:
            while True:
                want_update = self.docinput("\rDo you want to update to version "+new_version+"? [Y/n]", debug_it=False)
                if want_update == "Y":
                    self.debug.addEvent("updating to "+new_version, SYSTEM)
                    updater.tor_update()
<<<<<<< Updated upstream
                    break
=======
                    self.docprint(updater.getPath())
                    quit()
>>>>>>> Stashed changes

                elif want_update == "n":
                    self.debug.addEvent("user don't want to upgrade to version: "+new_version, SYSTEM)
                    break

                else:
                    self.debug.addEvent("Try again!", SYSTEM)
                    pass

        self.debug.addEvent("Listener Build...", SYSTEM)

        self.Listener = Listener.Listener()
        self.Listener.subclass = False
        self.Listener.ConsoleStart(self)

        self.debug.addEvent("Listener Build... Finished", SYSTEM)
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
                self.Listener.ConsoleExit(self, 400)
                quit()

        else:
            self.username = "USER"

    def log(self, command="docinputevent"):
        self.interpret.update()
        self.Listener.ConsoleRun(self, command=command, sender=self.sender)
        self.debug.addEvent(f"{command}", CONSOLE_IN)

        if command == "docinputevent":
            line_in = self.docinput(placeholder=f"[DOC][{self.username}]>>> ")

        else:
            line_in = command

        self.docprint(text=self.interpret.log(line_in))

    def docprint(self, text, end="\n", display_section=OUTPUT, debug_it=True):
        text = str(text)
        if debug_it:
            self.Listener.Print(self.instance, text=text)
            self.debug.addEvent("Docprint: " + text, str(display_section))

        if text == "None":
            pass

        else:
            sys.stdout.write(text + end)
            sys.stdout.flush()

    def docinput(self, placeholder="", debug_it=True, secure=False) -> str:
        # input
        self.docprint(placeholder, end="", debug_it=False)
        if secure:
            userinput = getpass.getpass("")
            return userinput

        userinput = sys.stdin.readline().replace("\n", "")

        if debug_it:
            self.debug.addEvent("Docinput: " + userinput, source=INPUT)
            self.Listener.UserInput(self, self.username, userinput)

        return userinput

    def client(self):
        self.Listener.TerminalClientStart(self)
        self.docprint("DOC-TERMINAL_CLIENT running DOC-" + version.version)
        try:
            while True:
                line_in = self.docinput(placeholder=f"[DOC][{self.username}]>>> ")
                if line_in.lower() != "exit":
                    self.docprint(self.log(line_in.lower()))
                    continue

                else:
                    self.Listener.TerminalClientStop(self, exitCode=200)
                    self.debug.addEvent("Console Exited", CONSOLE)
                    break

        except Exception as e:
            if not self.dev:
                self.docprint("Exit console")
                self.Listener.TerminalClientStop(self)
                self.debug.addEvent("Console Exited", CONSOLE)
                quit()

            else:
                raise e

    def getInstance(self):
        return self.instance

    def installPackage(self, packageName: str):
        path = f"plugins/{packageName}"
        self.Listener.PluginInstall(self, packageName, path)
        self.debug.addEvent("Install Package " + packageName + " from " + path, PLUGIN)
        exec(f"import core.plugins.{packageName}.DOC as {packageName}")


if __name__ == '__main__':
    this = doc(guest=False, username="Hallo", dev=True)
    this.client()
