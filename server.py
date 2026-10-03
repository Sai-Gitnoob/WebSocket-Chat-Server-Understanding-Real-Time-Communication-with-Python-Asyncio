"""Echo server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve
from aioconsole import ainput

connections = []

def connect (websocket):
    connections.append(websocket)
    print(f"The client {websocket} is connected and number of members in the connection is {len(connections)}")

def disconnect (websocket):
    connections.remove(websocket)
    print(f"The client {websocket} is disconnected and number of members in the connection is {len(connections)}")



async def broadcast_message(message):
    for websocket in connections:
        await websocket.send(f" {message} by ,{websocket}")

async def echo(websocket):
    connect(websocket)
    


    try:
        async for message in websocket:
            print(f"Received: {message}")
            await broadcast_message(message)
            message = await asyncio.to_thread(input, "> ")
            await websocket.send(message)
            if message.lower() == "exit":
                break
    finally:
        
        disconnect(websocket)


async def main():
    print("The server is running")
    server = await serve(echo, "localhost", 3000)
    await server.serve_forever()

    


if __name__ == "__main__":
    asyncio.run(main())