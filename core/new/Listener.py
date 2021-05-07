class Listener:
    def __init__(self):
        pass

    def UserInput(self, username: str, userinput: str):
        """get triggered, when a plugin want a Input from a User"""
        pass

    def Print(self, text: str):
        """get triggered, when a text print out"""
        pass

    def ConsoleRun(self, command: str, sender: str):
        """get triggered, when a command run"""
        pass

    def ConsoleExit(self, errorcode=200):
        """get triggered, when the Console stops. With a ErrorCode"""
        pass

    def ConsoleStart(self):
        """get triggered, when the Console Start"""
        pass

    def PluginInstall(self, pluginName: str, pluginPath: str):
        """get triggered, when Plugin get install"""
        pass

    def PluginUninstall(self, packageName: str):
        """get triggered, when Plugin get uninstall"""
        pass

    def TerminalClientStart(self):
        """get triggered, when user terminal start"""
        pass

    def TerminalClientStop(self, exitCode=200):
        """get triggered, when user terminal stop"""
        pass

    def CustomClientStart(self):
        """get triggered, when user terminal start"""
        pass

    def CustomClientStop(self, exitCode=200):
        """get triggered, when user terminal stop"""
        pass

    def commandUpdate(self):
        """get triggered, when commands get updated"""
        pass
