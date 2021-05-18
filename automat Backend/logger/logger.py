import logging
import sys
import globals

class logger:
    def start():
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
        datefmt="%H:%M:%S")
