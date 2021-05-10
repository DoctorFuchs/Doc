import time
from core.new import commands, debug, Listener, auth
from core.new.Interpret import interpreter


class doc:
    def __init__(self, username="USER", live_debug=False, guest=False):

        start = time.time()

        self.debug = debug.debug(live_debug=live_debug)

        self.debug.addEvent("Starting DOC...", "SYSTEM")
        self.debug.addEvent("Clear Commands...", "SYSTEM")

        commands.clear()

        self.debug.addEvent("Clear Commands... Finished", "SYSTEM")
        self.debug.addEvent("Create Variables...", "SYSTEM")

        # init names
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

        starttime = round((stop - start) * 1000) / 1000

        if starttime < 1:
            starttime = "under 1"

        self.debug.addEvent("DOC started in " + str(starttime) + " second(s)", self.system)

        if not guest:
            try:
                self.auth.login()

            except:
                self.docprint("login failed! exit")
                self.Listener.ConsoleExit(400)

    def log(self, command="docinputevent"):
        self.interpret.update()
        self.Listener.ConsoleRun(command=command, sender=self.sender)
        self.debug.addEvent(f"{command}", self.consoleInput)

        if command == "docinputevent":
            line_in = self.docinput(placeholder="[DOC]>>> ")

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

    def docinput(self, placeholder=""):
        # input
        userinput = input(placeholder + "")

        self.Listener.UserInput(self.username, userinput)

        return userinput

    def terminalclient(self, watchdog=True):
        self.Listener.TerminalClientStart()

        if watchdog:
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

            except:
                self.docprint("Exit console")
                self.Listener.TerminalClientStop()
                self.debug.addEvent("Console Exited", self.consoleGeneral)
                exit()

        else:
            while True:
                line_in = self.docinput(placeholder=f"[DOC][{self.username}]>>> ")
                if line_in.lower() != "exit":
                    self.docprint(self.log(line_in.lower()))
                    continue

                else:
                    self.Listener.TerminalClientStop(exitCode=200)
                    self.debug.addEvent("Console Exited", self.consoleGeneral)
                    break

    def getInstance(self):
        return self.instance

    def installPackage(self, packageName: str):
        path = f"plugins/{packageName}"
        self.Listener.PluginInstall(packageName, path)
        self.debug.addEvent("Install Package " + packageName + " from " + path, self.plugin)
        exec(f"import core.plugins.{packageName}.Main as {packageName}")
