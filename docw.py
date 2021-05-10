import sys

if sys.argv[1] == "core:run":
    from core.doc import doc

    try:
        username: str
        debug = False
        for i in range(len(sys.argv)):
            if "username:" in sys.argv[i]:
                username = sys.argv[i].replace("username:", "", 1)

            elif str(sys.argv[i]).startswith("debug:"):
                try:
                    debug = bool(sys.argv[i].replace("debug:", "", 1))

                except:
                    raise TypeError

        try:
            this = doc(username, live_debug=debug, guest=False)

        except NameError:
            print("""username  was not given, change to guest mode in guest mode debug is disabled""")
            raise NameError

    except NameError:
        this = doc("GUEST", guest=True)

    finally:
        this.terminalclient()

# add here new clients

else:
    print("""
Run client with:

python3 docw.py <client_name>:run

""")
