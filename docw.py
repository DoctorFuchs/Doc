import sys


def getArgument(argument: str, default="") -> str:
    for i in range(len(sys.argv)):
        if sys.argv[i].startswith(argument):
            try:
                return sys.argv[i].split(":", 1)[1]

            except:
                return default

    return default


def getArgumentAsBool(argument: str, default=False) -> bool:
    for i in range(len(sys.argv)):
        if sys.argv[i].startswith(argument):
            try:
                return bool(sys.argv[i].split(":", 1)[1])

            except:
                return default

    return default


if sys.argv[1] == "core:run":
    from core.doc import doc

    this = doc(
        username=getArgument(argument="username", default="USER"),
        live_debug=getArgumentAsBool(argument="debug"),
        guest=getArgumentAsBool("guest"),
        dev=getArgumentAsBool("dev")
    )

    this.client()
# add here new clients

else:
    print("""
Run client with:

python3 docw.py <client_name>:run <arguments>

""")
