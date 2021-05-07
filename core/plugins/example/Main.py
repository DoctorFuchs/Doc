from core.new import plugin

example_plugin = plugin.plugin("example")


@example_plugin.command("hello")
def sayHello():
    print("hello")


@example_plugin.command("echo", args=True)
def echo(args):
    del args[0]
    print(" ".join(args))
