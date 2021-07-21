from core.new.commands import addCommand


class plugin:
    def __init__(self, file):
        self.name = file.split("/")[len(file.split("/"))-1].replace(".py", "")

    def command(self, command: str):
        def function(code):
            addCommand(command=command, code=code, pluginName=self.name, runable=True)

        return function
