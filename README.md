# Doc
 
## Normal use

in the Doc/__init __.py you can init your doc consoles and start them

#### Commands for terminal client

`````text
pack <package Name> - install a package
echo <args>         - return args
exit                - exit the console
`````


#### Configuration

username:    Username of the user <br>
plugin:      Plugin-mode is only good for people testing Plugins <br>
live_debug:  Get Debug information's about the Doc console <br>

#### options of using Doc

`````python
import doc

test = doc.doc()

test.terminalclient() # starts the terminal client without the interface (maybe not available for unofficial Plugins)
test.interfaceclient() # starts the Interface client (maybe there are no interfaces available for Plugins)

test.installPackage("<package Name>") #if you want to start everytime with a package

test.log("command") #log a single command
`````

## Create Plugins

#### Main.py (in your plugin)
````python
import commands

commands.addCommand("<command name>", "<code or text>", pluginName="<Your pluginname>", runable=None)

#first argument = the command name: Attention maximum 1 word
#second argument = if you run code here runable have to be True. If you only want to return a text input your text here
# and runable have to be False. Attention: you can't use imports

#if you need in a function a argument you can use this for example:

commands.addCommand("echo", "args", pluginName="myPlugin", runable=True) #you need runable=True to use the variables

#useful variables:

#args:     - get the args as one String
#instance  - get the doc console that called your command
#instance.username - username of the user

#pluginName = input your pluginName here. Attention: this have to be the name of your main dictionary.
````

#### How to call this command

````html
[DOC]>>> <pluginName> <command> <args>
````