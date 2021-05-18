import globals
from dataset import dataset

def setButtons(button1 = "", button2 = "", button3 = ""):
    globals.socketdata.display.key1 = button1
    globals.socketdata.display.key2 = button2
    globals.socketdata.display.key3 = button3

def setScreen(screen = ""):
    globals.socketdata.display.screen = screen

def setTemperature(temp = 0.0):
    globals.socketdata.display.temperature=str(temp) + "°C"
