import asyncio
import websockets
import ipdb
import process


class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


async def run_server(websocket, path):
    data = await websocket.recv()
    print(f"received {data}")

    import ipdb; ipdb.set_trace()

    result = process.process(data)
    if type(result) == Exception:
        server_return = bcolors.FAIL + result.msg + bcolors.ENDC
    else:
        server_return = bcolors.OKGREEN + "success!" + bcolors.ENDC

    await websocket.send(server_return)

start_server = websockets.serve(run_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
