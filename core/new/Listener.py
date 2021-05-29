def check():
    subclasses = 0
    for i in range(len(Listener.__subclasses__())):
        if not Listener.__subclasses__()[i]().subclass:
            Listener.__subclasses__()[i]().subclass = True


class Listener:
    def __init__(self):
        self.subclass = True

    def UserInput(self, username: str, userinput: str):
        """get triggered, when a plugin want a Input from a User"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().UserInput(username, userinput)

    def Print(self, text: str):
        """get triggered, when a text print out"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().Print(text)

    def ConsoleRun(self, command: str, sender: str):
        """get triggered, when a command run"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().ConsoleRun(command, sender)

    def ConsoleExit(self, errorcode=200):
        """get triggered, when the Console stops. With a ErrorCode"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().ConsoleExit(errorcode)

    def ConsoleStart(self):
        """get triggered, when the Console Start"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().ConsoleStart()

    def PluginInstall(self, pluginName: str, pluginPath: str):
        """get triggered, when Plugin get install"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().PluginInstall(pluginName, pluginPath)

    def PluginUninstall(self, packageName: str):
        """get triggered, when Plugin get uninstall"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().PluginUninstall(packageName)

    def TerminalClientStart(self):
        """get triggered, when user terminal start"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().TerminalClientStart()

    def TerminalClientStop(self, exitCode=200):
        """get triggered, when user terminal stop"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().TerminalClientStop(exitCode)

    def CustomClientStart(self):
        """get triggered, when user terminal start"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().CustomClientStart()

    def CustomClientStop(self, exitCode=200):
        """get triggered, when user terminal stop"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().CustomClientStop(exitCode)

    def commandUpdate(self):
        """get triggered, when commands get updated"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().commandUpdate()
