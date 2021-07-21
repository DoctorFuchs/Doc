import importlib

from core.functions.system.getMainPath import getMainPath
from core.functions.system.hash import hash
from core.functions.system.getDictKeys import get_keys
from core.new import auths


class auth:
    def __init__(self, instance):
        self.instance = instance
        try:
            self.accounts = auths.accounts

        except:
            self.accounts = {}

        self.update()

    def auth(self, username, password):
        self.update()
        try:
            if self.accounts[username.lower()] == hash(password):
                return True

            else:
                return False

        except KeyError:
            return False

    def register(self, username, password):
        self.update()
        try:
            self.accounts[username.lower()] = hash(password)
            return True

        except KeyError:
            return False

    def isRegistered(self, username):
        self.update()
        if username.lower() in get_keys(self.accounts):
            return True

        else:
            return False

    def update(self):
        authfile = open(getMainPath() + "core/new/auths.py", "w")
        authfile.write(f"accounts ={self.accounts}")
        authfile.close()

    def login(self):
        if not self.isRegistered(self.instance.username):
            self.instance.docprint("This user is not registered! Sign up now!")
            self.instance.docprint("username: " + self.instance.username)
            self.register(self.instance.username, self.instance.docinput("password: ", secure=True))

        while True:
            if self.auth(self.instance.username, self.instance.docinput(f"{self.instance.username}'s password: ", secure=True)):
                self.instance.docprint("Success")
                break

            else:
                self.instance.docprint("Failed. Try Again!")
