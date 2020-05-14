import json

from config import WEBHOOKS_LOG_FILE


def log(file, data):
    # This could be done with standard python logging
    with open(file, "wb") as logfile:
        logfile.write(data)