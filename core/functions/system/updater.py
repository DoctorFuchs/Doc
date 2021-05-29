import requests as req

import version


def getGithubVersion() -> str:
    raw = req.get("https://raw.githubusercontent.com/DoctorFuchs/Doc/main/version.py") # request raw document
    if raw.status_code != 200: # if user is not online
        return version.version

    return raw.text.split("version = ")[1].split("<")[0].replace("\"", "")