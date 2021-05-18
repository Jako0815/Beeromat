import logging
import threading
import time
import asyncio
import json
import websockets
from types import SimpleNamespace
import sys
import globals
from logger.logger import logger
from config import config
from mysqlmodule import mysql_connector as mysql
from websocket import websocket
from dataset import dataset
from frontend import frontend
from logik import logik




if __name__ == "__main__":
    # Starte den Consolen logger
    logger.start()
    logging.info("Main    : Startup...")
    # Lese die Config Json ein...
    config.Read_Config()
    # Mit der MySQL Datenbank verbinden
    mysql.connect()

    globals.socketdata = dataset.Websocket_Data_Class()
    globals.socketdata.display=dataset.Display()
    globals.socketdata.externalcontroll = dataset.Automat_External_Controll()
    globals.socketdata.temperature = dataset.Automat_Temperature()
    globals.socketdata.sign = dataset.Automat_Schilder()

    globals.socketdata.ausgabe = []
    globals.socketdata.cashcontrollers = []
    globals.socketdata.fingersensors = []

    globals.socketdata.sps = dict()

    globals.modules = []

    frontend.setTemperature(0.0)
    frontend.setScreen("startup")
    frontend.setButtons("","","")

    logging.info("Main    : Stage builder part1 startup...")

    logging.info("Main    : Load Modules:")

    globals.dbcursor.execute("SELECT * FROM Module")
    myresult = globals.dbcursor.fetchall()
    for x in myresult:
        logging.info("StageBuilder    : ==============================================")
        logging.info("StageBuilder    : ID: " + str(x[0]) + ", Name: " + x[1] + ", Aktiviert: " + str(x[7]))

        if x[7] == 1:
            logging.info("StageBuilder    : Modul ID: " + str(x[0]) + " wird geladen...")

            data_config = json.loads(x[4])

            globals.dbcursor.execute("SELECT * FROM Basic_Module WHERE Name='" + str(x[2]) + "'")
            basic = globals.dbcursor.fetchall()

            globals.modules.append(dataset.Module_Loader(globals.config_data.websocket.host,globals.config_data.websocket.port,str(x[0]),str(x[3]),basic[0][2],basic[0][3],str(x[4]),str(x[5]),str(x[6]),str(x[8])))



            try:
                if data_config["finger"] == "w":
                    logging.info("StageBuilder    : Fingerabdruck erforderlich")
                    globals.socketdata.fingersensors.append(dataset.Automat_Fingerabdruck(str(x[0])))
            except KeyError:
                logging.info("StageBuilder    : Fingerabdruck nicht erforderlich")


            try:
                if data_config["ausgabe"] == "w":
                    logging.info("StageBuilder    : Automaten Ausgabe erforderlich")
                    globals.socketdata.ausgabe.append(dataset.Automat_Ausgabe(str(x[0])))
            except KeyError:
                logging.info("StageBuilder    : Automaten Ausgabe nicht erforderlich")


            try:
                if data_config["cash"] == "w":
                    logging.info("StageBuilder    : Cashcontroller erforderlich")
                    globals.socketdata.cashcontrollers.append(dataset.Automat_Cashcontroller(str(x[0])))
            except KeyError:
                logging.info("StageBuilder    : Cashcontroller Zugriff nicht erforderlich")


            try:
                if data_config["sps"] == "w":
                    logging.info("StageBuilder    : Modul benötigt Schreib Zugriff auf SPS")
                elif data_config["sps"] == "r":
                    logging.info("StageBuilder    : Modul benötigt Lese Zugriff auf SPS")
            except KeyError:
                logging.info("StageBuilder    : SPS Zugriff nicht erforderlich")

            var_config = json.loads(x[5])


            for x in var_config:
                logging.info("StageBuilder    : SPS Variable: " + list(x.keys())[0] + " Zugriff: " + list(x.values())[0])
                if globals.socketdata.sps.get(list(x.keys())[0]) == list(x.values())[0]:
                    if list(x.values())[0] == "w":
                        logging.info("StageBuilder    : ERROR Doppelter Schreibzugriff auf: " + list(x.keys())[0])
                        exit()

                if list(x.values())[0] == "r":
                    if globals.socketdata.sps.get(list(x.keys())[0]) == "w":
                        logging.info("StageBuilder    : Variable ist auf write, überspringe schreiben...")
                    else:
                        globals.socketdata.sps.update({list(x.keys())[0]: list(x.values())[0]})
                else:
                    globals.socketdata.sps.update({list(x.keys())[0]: list(x.values())[0]})
        logging.info("StageBuilder    : ==============================================")

    logging.info("StageBuilder    : Module wurden Erfolgreich geladen")
    logging.info("StageBuilder    : Datenset wurde erzeugt.")
    logging.info("StageBuilder2    : Starte nächste Stufe des StageBuilders...")


    logik = threading.Thread(target=logik.logik_main, args=())

    logik.start()


    logging.info("Main    : Starte den Socket...")

    websocket.Socket_Start()
