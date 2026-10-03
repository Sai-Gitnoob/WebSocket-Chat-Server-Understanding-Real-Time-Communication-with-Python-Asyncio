#!/usr/bin/env python

"""Client using the asyncio API."""

import asyncio
from websockets.asyncio.client import connect


async def hello():
        async with connect("ws://localhost:3000") as websocket:
            async def receive():
                 async for message in websocket:
                      print(f"Recieved the message : {message}")
            receiver = asyncio.create_task(receive())

            try:
                while True:
                    message = await asyncio.to_thread(input, "> ")
                    await websocket.send(message)
                    if message.lower() == "exit":
                        break

                

            finally:
                receiver.cancel()


if __name__ == "__main__":
    asyncio.run(hello())