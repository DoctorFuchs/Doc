import time

from core.functions.system.Sections import *


class debug:
    def __init__(self, instance, live_debug=False):
        self.history = []
        self.live = live_debug
        self.instance = instance
        self.start = False

    def get(self, event: str) -> str:
        length = len(event)
        adder = " " * (100 - length) + "|"
        return event + adder

    def addEvent(self, event: str, source: str):
        message = "[" + time.ctime() + "]>>> " + self.get(event) + "\t" + source
        self.history.append(message)

        if event == "Docprint: None":
            return

        if self.live:
            try:
                self.instance.docprint(message, display_section=DEBUG, debug_it=False)

            except:
                pass

        elif self.start:
            self.instance.docprint("\r"+event, end="", debug_it=False)

    def view(self):
        for i in range(len(self.history)):
            self.instance.docprint(self.history[i], display_section=DEBUG, debug_it=False)
