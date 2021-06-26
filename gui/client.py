import sys
import os
import webbrowser

from flask import Flask

sys.path.append(str(os.path.dirname(os.path.abspath(__file__))).replace("Doc/core", "Doc"))

from core import doc

app = Flask(__name__)
client = doc.doc(guest=True)


@app.route("/")
def index():
    html_file = open("HTML/index.html")
    return "\n".join(html_file.readlines())


if __name__ == '__main__' or __name__ == 'docw':
    webbrowser.open("127.0.0.1:5000")
    app.run("127.0.0.1", 5000)



