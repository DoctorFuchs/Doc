# Doc

#### Need more help?
[Join our Discord](https://www.discord.com/invite/KApyCPDpDx)

## Normal use

#### Commands for terminal client

`````text
pack <package Name> - install a package
packs               - view all installable packages
h <searchstring>    - search for a help helps 
`````


#### Configuration

username:    Username of the user (with login) <br>
live_debug:  Get Debug information's about the Doc console <br>
dev: raise errors and exit
guest: no login, but no saves

#### options of using Doc

`````python
from core import doc

test = doc.doc()
test.log("<command>")  # logs a single command to this doc console
test.client()  # starts the client (default: terminal)
`````

## Plugin creating

#### create a command

```python
# your DOC.py file

from core.new import plugin

this_plugin = plugin.plugin("<name from the dict of this file>")

@this_plugin.command("command")
def command():
    pass

@this_plugin.command("print", instance=True) #create a command with get input and print something out
def print_com(instance):
    instance.docprint("hello i am a command, say me hello!")
    instance.docinput(placeholder="hello? ")
    

@this_plugin.command("args", args=True) # create a plugin get the arguments
def args_parser(args):
    if args is not []:
        args.clear()

@this_plugin.command("echo", args=True, instance=True) # you can combine this 
def echo(args, instance): # attention don't change args, instance -> instance, args
    del args[0]  # args[0] is to 100% echo
    instance.docprint(" ".join(args))
```

#### create a Listener
````python
from core.new import Listener

class example_listener(Listener):
    def __init__(self):
        super().__init__()
    
    # for example
    def ConsoleRun(self, command: str, sender: str):
        super().instance.docprint("execute: " + command)
````
