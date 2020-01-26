import asyncio
import websockets
import ipdb

import process

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
    server_return = f"{result}"
    await websocket.send(server_return)

start_server = websockets.serve(run_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
