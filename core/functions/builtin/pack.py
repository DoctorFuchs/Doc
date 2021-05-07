def pack(args: list, instance):
    """install packages"""
    try:
        instance.instance.installPackage(args[0])
        instance.instance.installed.append(args[0])

    except:
        if args[0] is None:
            args[0] = " "

        instance.instance.docprint("no package available named " + args[0], consoleOutput=True)
