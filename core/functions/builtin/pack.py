from core.functions.system.Sections import CONSOLE


def pack(event):
    """install packages"""
    try:
        event.__installPackage__(event.args[0])
        event.installed.append(event.args[0])
        event.print("Successful installed Plugin "+event.args[0])

    except OSError:
        try:
            if event.args[0] is None:
                event.args[0] = " "

        except:
            event.args = [" "]

        event.print("no package available named " + event.args[0], display_section=CONSOLE)
