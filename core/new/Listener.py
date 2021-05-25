class Listener:
    def __init__(self):
        pass

    def UserInput(self, username: str, userinput: str):
        """get triggered, when a plugin want a Input from a User"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().UserInput(username, userinput)

    def Print(self, text: str):
        """get triggered, when a text print out"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().Print(text)

    def ConsoleRun(self, command: str, sender: str):
        """get triggered, when a command run"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().ConsoleRun(command, sender)

    def ConsoleExit(self, errorcode=200):
        """get triggered, when the Console stops. With a ErrorCode"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().ConsoleExit(errorcode)

    def ConsoleStart(self):
        """get triggered, when the Console Start"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().ConsoleStart()

    def PluginInstall(self, pluginName: str, pluginPath: str):
        """get triggered, when Plugin get install"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().PluginInstall(pluginName, pluginPath)

    def PluginUninstall(self, packageName: str):
        """get triggered, when Plugin get uninstall"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().PluginUninstall(packageName)

    def TerminalClientStart(self):
        """get triggered, when user terminal start"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().TerminalClientStart()

    def TerminalClientStop(self, exitCode=200):
        """get triggered, when user terminal stop"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().TerminalClientStop(exitCode)

    def CustomClientStart(self):
        """get triggered, when user terminal start"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().CustomClientStart()

    def CustomClientStop(self, exitCode=200):
        """get triggered, when user terminal stop"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().CustomClientStop(exitCode)

    def commandUpdate(self):
        """get triggered, when commands get updated"""
        if issubclass(Listener, self.__class__):
            return

        for i in range(len(Listener.__subclasses__())):
            Listener.__subclasses__()[i]().commandUpdate()
