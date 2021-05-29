from core.new.commands import addCommand


class plugin:
    def __init__(self, name):
        self.name = name

    def command(self, command: str, args=False, instance=False):
        needArgs = []
        if args:
            needArgs.append("args")

        if instance:
            needArgs.append("instance")

        def function(code):
            addCommand(command=command, code=code, pluginName=self.name, runable=True, needArgs=needArgs)

        return function
