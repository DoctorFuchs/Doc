def debug(event):
    """debug output on/off or view"""
    if len(event.args) == 0:
        event.print("usage: debug <mode> \nmodes: \n\ton: turns debug on\n\toff: turns debug off\n")

    elif event.args[0] == "off":
        event.Debug.live = False
        event.print("debug output is now off")

    elif event.args[0] == "on":
        event.Debug.live = True
        event.print("debug output is now on")

    elif event.args[0] == "view":
        event.debug.view()

    else:
        event.print("usage: debug <mode> \nmodes: \n\ton: turns debug on\n\toff: turns debug off\nview: view the recent debug\n")