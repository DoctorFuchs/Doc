def listener(event):
    """listener output on/off"""
    if len(event.args) == 0:
        event.print("usage: listener <mode> \nmodes: \n\ton: turns listener on\n\toff: turns listener off\n")

    elif event.args[0] == "on":
        event.Listener.subclass = False
        event.print("listener output is now on")

    elif event.args[0] == "off":
        event.Listener.subclass = True
        event.print("listener output is now off")

    else:
        event.print("usage: listener <mode> \nmodes: \n\ton: turns listener on\n\toff: turns listener off\n")