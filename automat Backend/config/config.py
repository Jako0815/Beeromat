import json
from types import SimpleNamespace
import logging
import sys
import globals
import __main__

def Read_Config():
    logging.info("Config-Reader    : Lese Configuration")
    config_file = open("config_files/mainconfig.json","r")
    config_data = json.loads(config_file.read(), object_hook=lambda d: SimpleNamespace(**d))
    globals.config_data = config_data
    logging.info('=== Websocket Konfiguration ===')
    logging.info('Port: ' + config_data.websocket.port)
    logging.info('IP: ' + config_data.websocket.host)

    logging.info('=== MySQL Konfiguration ===')
    logging.info('IP: ' + config_data.mysql.host)
    logging.info('Username: ' + config_data.mysql.username)
    if len(config_data.mysql.password) > 0:
      logging.info('Passwort: (versteckt)')
    else:
      logging.info('Passwort: (nicht vorhanden)')
