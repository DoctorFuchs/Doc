import os
from core.new import commands

def packs(args: list, instance):
    """view plugins"""
    args = " ".join(args)
    blocked = [".DS_Store", "__pycache__", "__init__.py", "PluginCommands.txt", "plugincodes.py"]
    plugins = os.listdir(commands.getMainPath() + 'core/plugins')

    print("Available Plugins:\n")

    for i in range(len(plugins)):
        if plugins[i] in blocked:
            pass

        elif args in " ":
            instance.docprint(plugins[i])

        elif args in plugins[i]:
            instance.docprint(plugins[i])

    print("\ninstall plugins with 'pack <plugin_name>'\n")
