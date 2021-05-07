import time


class debug:
    def __init__(self, live_debug=False):
        self.history = []
        self.live = live_debug

    def get(self, event:str):
        length = len(event)
        adder = " " * (100 - length) + "|"
        return event + adder

    def addEvent(self, event:str, source:str):
        message = "[" + time.ctime() + "]>>> " + self.get(event) + "\t" + source
        self.history.append(message)

        if self.live:
            print(message)

    def view(self):
        for i in range(len(self.history)):
            print(self.history[i])
