from core.new import plugin

clockplugin = plugin.plugin("clock")


@clockplugin.command("c", instance=True)
def clock(instance):
    """live time clock"""
    import time, datetime
    try:
        while True:
            instance.docprint("\r" + datetime.datetime.now().strftime("%H:%M:%S"), end="")
            time.sleep(1)

    except:
        instance.docprint("", end="\n")
