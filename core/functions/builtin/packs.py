import os
from core.new import commands


def packs(event):
    """view plugins"""
    args = " ".join(event.args)
    verified = ["clock_1", "example"]
    blocked = [".DS_Store", "__pycache__", "__init__.py", "PluginCommands.txt", "plugincodes.py", "verified.py"]
    plugins = os.listdir(commands.getMainPath() + 'core/plugins')
    v_text = ""

    event.print("Available Plugins:\n")

    for i in range(len(plugins)):
        if plugins[i] in verified:
            v_text = "\u2713"

        else:
            v_text = ""

        if plugins[i] in blocked:
            pass

        elif args in " ":
            event.print(plugins[i]+" "+v_text)

        elif args in plugins[i]:
            event.print(plugins[i]+" "+v_text)

    event.print("\ninstall plugins with 'pack <plugin_name>'\n")
