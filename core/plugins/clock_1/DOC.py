from core.new import plugin

clockplugin = plugin.plugin("clock_1")


@clockplugin.command("c", instance=True)
def clock(instance):
    """live time clock_1"""
    import time, datetime
    try:
        while True:
            instance.docprint("\r" + str(datetime.datetime.now().strftime("%H:%M:%S")), end="")
            time.sleep(1)

    except:
        instance.docprint("", end="\n")
