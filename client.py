import asyncio
import websockets
import websocket as wb_client

async def hello():
    uri = "ws://localhost:8765"
    header = ["User-Agent: MyProgram","x-custom: header"]
    async with wb_client.connect(uri, timeout=None, class_=wb_client.WebSocket, header=header) as websocket:
        data = input("mydatabase client >>>> ")

        if "\\c" in data:
            db_name = data.split(" ")[1]
            header.append(f"database_name: {db_name}")

        await websocket.send(data)
        print(f">>>> {data}")

        back_from_server = await websocket.recv()
        print(back_from_server)

asyncio.get_event_loop().run_until_complete(hello())
