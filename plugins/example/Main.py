import commands

code = """plugins.example.Main.p()"""

commands.addCommand("hallo", code=code, pluginName="example", runable=True)


def p():
    print("hallo")