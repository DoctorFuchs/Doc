from core.new import plugin
from core.new.Listener import Listener

example_plugin = plugin.plugin("example")


@example_plugin.command("hello", instance=True)
def sayHello(instance):
    instance.docprint("hello")


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