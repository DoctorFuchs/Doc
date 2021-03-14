from Listener import Listener
import time
import commands
from plugins import *

try:
    import colorama
    from colorama import Fore as color
    color.__init__()

except ImportError or ImportWarning:
    print("install colorama for colored text")
    class color:
        RED = ""
        BLUE = ""
        GREEN = ""
        WHITE = ""
        BLACK = ""
        MAGENTA = ""
        CYAN = ""
        YELLOW = ""

class debug:
    def __init__(self, live_debug=False):
        self.history = []
        self.live = live_debug

    def get(self, event):
        length =len(event)
        adder=" "*(100-length)+"|"
        return (event+adder)
        

    def addEvent(self, event, source):
        message = "["+time.ctime()+"]>>> "+self.get(event)+"\t"+source
        self.history.append(message)

        if self.live == True:
            print(message)

    def view(self):
        for i in range(len(self.history)):
            print(self.history[i])

class doc:
    def __init__(self, username="USER", plugin=False, live_debug = False):
        start = time.time()
        
        self.debug = debug(live_debug=live_debug)
        
        self.debug.addEvent("Starting DOC...", "SYSTEM")
        self.debug.addEvent("Create Variables...", "SYSTEM")

        #init names
        self.username = username
        self.user = "USER:"+self.username
        self.plugin = "PLUGIN"
        self.consoleGeneral = "CONSOLE"
        self.system = "SYSTEM"
        self.consoleGeneral = "CONSOLE"
        self.consoleInput = "CONSOLE IN"
        self.consoleOutput = "CONSOLE OUT"

        instance = self
        
        self.debug.addEvent("Create Variables...Finished", self.system)
        self.debug.addEvent("Listener Build...", self.system)

        self.Listener = Listener()
        self.Listener.ConsoleStart()

        self.debug.addEvent("Listener Build... Finished", self.system)
        self.debug.addEvent("Interpret Build...", self.system)
        self.interpret = interpret(instance)
        self.debug.addEvent("Interpret Build... Finished", self.system)
        
        
        self.pluginMode = plugin

        if self.pluginMode == True:
            self.sender = self.plugin

        elif __name__ == "system":
            self.sender = self.system

        else:
            self.sender = self.user

        self.debug.addEvent("Starting DOC... Finished", self.system)

        stop = time.time()
        
        starttime = round((stop-start)*1000)/1000
        
        if starttime<1:
            starttime = "under 1"
        
        
        self.debug.addEvent("DOC started in "+str(starttime)+" second(s)", self.system)

    def getInstance(self):
        return self

    def docprint(self, text, consoleOutput=False):
        text = str(text)
        self.Listener.Print(text=text)
        if consoleOutput:
            self.debug.addEvent("Output: "+text, self.consoleOutput)

        if text == "None":
            pass

        else:
            print(text)

    def docinput(self, placeholder=""):
        #input
        userinput = input(placeholder+"")

        self.Listener.UserInput(self.username, userinput)
        
        return userinput
        
    def log(self, command="docinputevent"):
        self.interpret.update()
        self.Listener.ConsoleRun(command=command, sender=self.sender)
        self.debug.addEvent(f"{command}", self.consoleInput)

        if command == "docinputevent":
            line_in = self.docinput(placeholder="[DOC]>>> ")
        
        else:
            line_in = command
        
        self.docprint(text=self.interpret.log(line_in), consoleOutput=True)

    def interfaceclient(self):
        pass

    def terminalclient(self):
        self.Listener.TerminalClientStart()
        while True:
            line_in = self.docinput(placeholder=f"[DOC][{self.username}]>>> ")
            if line_in.lower() != "exit":
                self.log(line_in.lower())
                continue
            
            else:
                self.Listener.TerminalClientStop(exitCode=200)
                self.debug.addEvent("Console Exited", self.consoleGeneral)
                break

    def installPackage(self, path, packageName):
        self.Listener.PluginInstall(packageName, path)
        self.debug.addEvent("Install Package "+packageName+" from "+path, self.plugin)

    def uninstallPackage(self, packageName):
        self.Listener.PluginUninstall(packageName)
        self.debug.addEvent("Uninstall Package "+packageName, self.plugin) 
        
    def getPluginCommands(self):
        return self.PluginCommands

class interpret:
    def __init__(self, instance):
        self.commands = commands.getCommands()
        self.instance = instance

    def update(self):
        self.commands = commands.getCommands()

    def log(self, command):
        self.instance.debug.addEvent(event="Update Plugin Commands", source="PLUGINLOG")
        self.instance.Listener.commandUpdate()
        commands.update()
        
        com = ""
        try:
            c = command.split()
            
            com = c[0].lower()

            del(c[0])
            args = c

        except:
            pass

        if com in " ":
            pass

        elif com in self.commands:
            objekt = self.commands[com]
            return eval(objekt)
        
        else:
            return "no command named "+com

#Systemcommands
def echo(args):
    return str(" ".join(args))

def pack(args, instance):
    instance.installPackage(args[0], args[1]) 


#TODO more Systemcommands

doc1 = doc(username="Paul", plugin=False, live_debug=True)
doc1.terminalclient()
