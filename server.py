import asyncio
import websockets
import ipdb

import process

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


async def run_server(websocket, path):
    data = await websocket.recv()
    print(f"received {data}")

    # for sql:
    #   -> need to parse string
    #   -> validate string
    # if valid, do appropriate operation:
    #   -> create/drop database
    #   -> create/drop/alter table
    #   -> save data to CSV file
    #   -> select some data

    result = process.process(data)
    if type(result) == Exception:
        server_return = bcolors.FAIL + result.msg + bcolors.ENDC
    else:
        server_return = bcolors.OKGREEN + "success!" + bcolors.ENDC

    await websocket.send(server_return)

start_server = websockets.serve(run_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
