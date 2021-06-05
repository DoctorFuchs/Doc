def clock(instance):
    """live time clock"""
    import time, datetime
    try:
        while True:
            instance.docprint("\r" + str(datetime.datetime.now().strftime("%H:%M:%S")), end="")
            time.sleep(1)

    except:
        instance.docprint("", end="\n")
