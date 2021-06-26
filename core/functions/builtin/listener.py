def listener(args: list, instance):
    """listener output on/off"""
    if len(args) == 0:
        instance.docprint("usage: listener <mode> \nmodes: \n\ton: turns listener on\n\toff: turns listener off\n")

    elif args[0] == "on":
        instance.Listener.subclass = False
        instance.docprint("listener output is now on")

    elif args[0] == "off":
        instance.Listener.subclass = True
        instance.docprint("listener output is now off")

    else:
        instance.docprint("usage: listener <mode> \nmodes: \n\ton: turns listener on\n\toff: turns listener off\n")