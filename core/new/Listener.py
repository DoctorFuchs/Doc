def check():
    subclasses = 0
    for i in range(len(Listener.__subclasses__())):
        if not Listener.__subclasses__()[i]().subclass:
            Listener.__subclasses__()[i]().subclass = True


class Listener:
    def __init__(self):
        self.subclass = True

    def UserInput(self, console, username: str, userinput: str):
        """get triggered, when a plugin want a Input from a User"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().UserInput(console, username, userinput)

    def Print(self, console, text: str):
        """get triggered, when a text print out"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().Print(console, text)

    def ConsoleRun(self, console, command: str, sender: str):
        """get triggered, when a command run"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().ConsoleRun(console, command, sender)

    def ConsoleExit(self, console, errorcode=200):
        """get triggered, when the Console stops."""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().ConsoleExit(console, errorcode)

    def ConsoleStart(self, console):
        """get triggered, when the Console Start"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().ConsoleStart(console)

    def PluginInstall(self, console, pluginName: str, pluginPath: str):
        """get triggered, when Plugin get install"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().PluginInstall(console, pluginName, pluginPath)

    def PluginUninstall(self, console, packageName: str):
        """get triggered, when Plugin get uninstall"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().PluginUninstall(console, packageName)

    def TerminalClientStart(self, console):
        """get triggered, when user terminal start"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().TerminalClientStart(console)

    def TerminalClientStop(self, console, exitCode=200):
        """get triggered, when user terminal stop"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().TerminalClientStop(console, exitCode)

    def CustomClientStart(self, console):
        """get triggered, when user terminal start"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().CustomClientStart(console)

    def CustomClientStop(self, console, exitCode=200):
        """get triggered, when user terminal stop"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().CustomClientStop(console, exitCode)

    def commandUpdate(self, console):
        """get triggered, when commands get updated"""
        check()
        if self.subclass:
            return

        for i in range(len(Listener.__subclasses__())):
            if Listener.__subclasses__()[i]().subclass:
                Listener.__subclasses__()[i]().commandUpdate(console)
