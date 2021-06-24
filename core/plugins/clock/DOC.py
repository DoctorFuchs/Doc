from core.new import plugin

clockplugin = plugin.plugin("clock")


@clockplugin.command("time", instance=True)
def clock(instance):
    """live time clock"""
    import time, datetime
    try:
        while True:
            instance.docprint("\r" + str(datetime.datetime.now().strftime("%H:%M:%S")), end="")
            time.sleep(1)

    except:
        instance.docprint("", end="\n")

@clockplugin.command("cd", args=True, instance=True)
def countdown(args, instance):
	"""countdown"""
	import time
	try:
		times = int(args[1])
		while True:
			if times <= 0.0:
				instance.docprint(f"\rFinished ({int(args[1])})\n", end="")
				break
			time.sleep(0.1)
			times -= 0.1
			instance.docprint(f"\r{round(times*10)/10}", end="")

	except ValueError:
		instance.docprint("usage: clock cd <time>")
	