# Doc
 
## Normal use

#### Commands for terminal client

`````text
pack <package Name> - install a package
packs               - view all installable packages
h <serachstring>    - search for a help helps 
`````


#### Configuration

username:    Username of the user <br>
live_debug:  Get Debug information's about the Doc console <br>

#### options of using Doc

`````python
from core import doc

test = doc.doc()
test.log("<command>")  # log a single command
test.terminalclient()  # starts the terminal client without the interface (maybe not available for unofficial Plugins)
`````
