from core.new.plugin import plugin

this = plugin("example_1")


@this.command("test")
def test(event):
    event.print("hallo")
