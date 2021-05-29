from core.functions.system.Sections import CONSOLE


def pack(args: list, instance):
    """install packages"""
    try:
        instance.instance.installPackage(args[0])
        instance.instance.installed.append(args[0])
        instance.instance.docprint("Successful installed Plugin "+args[0])

    except:
        try:
            if args[0] is None:
                args[0] = " "

        except:
            args = [" "]

        instance.instance.docprint("no package available named " + args[0], display_section=CONSOLE)
