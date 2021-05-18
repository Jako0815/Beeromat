#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import websockets
from types import SimpleNamespace
from logger.logger import logger
import logging
import sys
import globals
import __main__

from dataset.dataset import *


import json

def Encode_Data():
    output = globals.socketdata.toJSON()

    return output


USERS = set()

def users_event():
    return Encode_Data()


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(users_event())
        async for message in websocket:
            data = json.loads(message)

    finally:
        await unregister(websocket)


def Socket_Start():
  start_server = websockets.serve(counter, globals.config_data.websocket.host, globals.config_data.websocket.port)
  asyncio.get_event_loop().run_until_complete(start_server)
  logging.info("Main    : Startup...")
  asyncio.get_event_loop().run_forever()
