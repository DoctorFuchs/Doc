import time

from core.functions.system.Sections import *


class debug:
    def __init__(self, instance, live_debug=False):
        self.history = []
        self.live = live_debug
        self.instance = instance
        self.start = False

    def get(self, event:str):
        length = len(event)
        adder = " " * (100 - length) + "|"
        return event + adder

    def addEvent(self, event:str, source:str):
        message = "[" + time.ctime() + "]>>> " + self.get(event) + "\t" + source
        self.history.append(message)

        if self.live:
            self.instance.docprint(message, DEBUG)

        elif self.start:
            self.instance.docprint("\r"+event, end="", debug_it=False)

    def view(self):
        for i in range(len(self.history)):
            self.instance.docprint(self.history[i], section=OUTPUT, debug_it=False)
