from core.new import plugin
from core.new.Listener import Listener

example_plugin = plugin.plugin("example")


@example_plugin.command("version")
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


@example_plugin.command("echo_2", args=True)
def echo(args):
    del args[0]  # args[0] is to 100% echo
    return " ".join(args)


@example_plugin.command("test")
def test():
    print("test")


class example_listener(Listener):
    def __init__(self):
        super().__init__()

    def ConsoleRun(self, console, command: str, sender: str):
        console.docprint("execute: " + command)
