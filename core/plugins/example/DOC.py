from core.new import plugin
from core.new.Listener import Listener

example_plugin = plugin.plugin("example")


@example_plugin.command("version", instance=True)
def example(instance):
    import version  # use local imports
    instance.docprint("print " + version.version)  # use docprint() to print on all clients


@example_plugin.command("hello", instance=True)
def sayHello(instance):
    instance.docprint("hello")


@example_plugin.command("echo", args=True, instance=True)
def echo(args, instance):
    del args[0]  # args[0] is to 100% echo
    instance.docprint(" ".join(args))


class example_listener(Listener):
    def __init__(self):
        super().__init__()

    def ConsoleRun(self, command: str, sender: str):
        print("execute: " + command)
