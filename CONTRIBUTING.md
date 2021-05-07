# CONTRIBUTING

## RULES

Test your changes!
In future I will add a test client for testing plugins :-)

## Creating Plugins

````python
# in Main.py
# Init the plugin
from core.new import plugin

yourPlugin = plugin.plugin("plugin_name") # plugin_name have to be the dict name 

# add a command
@yourPlugin.command("command")
def yourFunction():
    print("this is your command")

# add a command using args the same with instance
@yourPlugin.command("withargs", args=True)
def functionwithargs(args):
    del args[0] # the first argument is the function name (here "withargs")
    print("this was your args: "+" ".join(args))
````

```commandline
[DOC][Example]>>> pack plugin_name  
[DOC][Example]>>> plugin_name command
this is your command
[DOC][Example]>>> plugin_name withargs hello and welcome
this was your args: hello and welcome
```

## args

args -> list <br>
args contains not the main command!

````commandline
[DOC][Example]>>> command args[0] args[1] args[2]...
````

## instance

instance -> doc-console <br>
instance is used to get the configured doc console