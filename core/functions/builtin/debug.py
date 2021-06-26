def debug(args: list, instance):
    """debug output on/off or view"""
    if len(args) == 0:
        instance.docprint("usage: debug <mode> \nmodes: \n\ton: turns debug on\n\toff: turns debug off\n")

    elif args[0] == "off":
        instance.debug.live = False
        instance.docprint("debug output is now off")

    elif args[0] == "on":
        instance.debug.live = True
        instance.docprint("debug output is now on")

    elif args[0] == "view":
        instance.debug.view()

    else:
        instance.docprint("usage: debug <mode> \nmodes: \n\ton: turns debug on\n\toff: turns debug off\nview: view the recent debug\n")