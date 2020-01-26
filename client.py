import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        data = input("mydatabase client >>>> ")

        await websocket.send(data)
        print(f">>>> {data}")

        back_from_server = await websocket.recv()
        print(back_from_server)

asyncio.get_event_loop().run_until_complete(hello())
