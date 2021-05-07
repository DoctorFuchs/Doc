from core.new import commands as com
import wikipedia

searchcode = "plugins.wiki.Main.search(args)"

com.addCommand("search", searchcode, "wiki", runable=True)


def search(args):
    del args[0]
    page = wikipedia.search(" ".join(args))
    try:
        return page

    except wikipedia.exceptions.DisambiguationError:
        return "sorry "
