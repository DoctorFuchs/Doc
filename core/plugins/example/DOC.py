from core.new import plugin
from core.new.Listener import Listener

example_plugin = plugin.plugin("example")


@example_plugin.command("hello", instance=True)
def sayHello(instance):
    from core.new.Listener import Listener
    instance.docprint("hello")
    print(Listener.__subclasses__())


@example_plugin.command("echo", args=True, instance=True)
def echo(args, instance):
    del args[0]
    instance.docprint(" ".join(args))


@example_plugin.command("subs", instance=True)
def subs(instance):
    instance.docprint(instance.Listener.__subclass__())


class example_listener(Listener):
    def __init__(self):
        super().__init__()

    def ConsoleRun(self, command: str, sender: str):
        print("execute: " + command)

    def UserInput(self, username: str, userinput: str):
        print(f"userinput from {username}: "+userinput)

    def commandUpdate(self):
        print("lone")
