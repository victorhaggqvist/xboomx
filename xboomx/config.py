import os
import json
import logging


def load_config():
    try:
        with open(os.getenv("HOME") + "/.xboomx/config") as config_file:
            return json.loads('\n'.join(config_file.readlines()))
    except:
        logging.error("Failed to load config file")
        return {}


config = load_config()
