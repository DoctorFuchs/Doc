import core.new.commands as coms
from core.functions.system.getDictKeys import get_keys
import os
from core import plugins
from core.functions.system.getMainPath import getMainPath

for i in range(len(os.listdir(getMainPath() + "core/functions/builtin"))):
    if os.listdir(getMainPath() + "core/functions/builtin")[i].endswith(".py"):
        exec("from core.functions.builtin import " + os.listdir(getMainPath() + "core/functions/builtin")[i].replace(".py", ""))


def h(event) -> str:
    """print a help"""
    coms.update()
    searchstring = ""

    if event.args:
        searchstring = " ".join(args)

    keys = get_keys(coms.getCommands())
    keys.sort()

    output = """commands:\n"""
    for i in range(len(keys)):
        if keys[i] == " ":
            continue

        helper = coms.getCommands()[keys[i]].split("(", 1)[0] + ".__doc__"

        if helper == "h.h.__doc__":
            helper = "h.__doc__"

        help_text = eval(helper)
        if help_text is None:
            help_text = "No description available"

        if searchstring in get_keys(coms.getCommands())[i]:
            output += f"""\t{keys[i]}: {help_text}\n"""

    return output
