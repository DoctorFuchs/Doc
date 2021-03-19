import commands

code = """print("your code")"""

commands.addCommand("hallo", code=code, pluginName="example", runable=True)

def p():
    print("hallo")
