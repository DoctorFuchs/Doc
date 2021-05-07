import core.new.commands as coms
from core.functions.system.getDictKeys import get_keys
import os
from core import plugins
from core.functions.system.getMainPath import getMainPath

for i in range(len(os.listdir(getMainPath() + "core/functions/builtin"))):
    exec("from core.functions.builtin import " + os.listdir(getMainPath() + "core/functions/builtin")[i].replace(".py",""))


def h(args: list, instance):
    """print this help"""
    coms.update()
    searchstring = ""

    if args != []:
        searchstring = " ".join(args)

    output = """commands:\n"""
    for i in range(len(get_keys(coms.getCommands()))):
        if get_keys(coms.getCommands())[i] == " ":
            continue

        helper = coms.getCommands()[get_keys(coms.getCommands())[i]].split("(", 1)[0] + ".__doc__"

        if helper == "h.h.__doc__":
            helper = "h.__doc__"

        if searchstring in get_keys(coms.getCommands())[i]:
            output += f"""\t{get_keys(coms.getCommands())[i]}:{eval(helper)}\n"""

    return output
