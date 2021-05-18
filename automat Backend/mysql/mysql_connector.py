#!/usr/bin/env python

# Mysql Connector für Automat
import globals
import __main__
import json
import mysql.connector


def connect():
    globals.automatdb = mysql.connector.connect(
    host=globals.config_data.mysql.host,
    user=globals.config_data.mysql.username,
    password=globals.config_data.mysql.password
  )
