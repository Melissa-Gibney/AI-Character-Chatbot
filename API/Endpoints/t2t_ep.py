import asyncio
import json
import websockets
from event import subscribe, postEvent

async def t2tEndpoint(websocket):
    recieveT2TResponseTask = asyncio.create_task(recieveT2TResponse(websocket))
    sendT2TRequestTask = asyncio.create_task(sendT2TRequest(websocket, None))
    done, pending = await asyncio.wait(
        [recieveT2TResponseTask, sendT2TRequestTask],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        print(task)
        task.cancel()

async def recieveT2TResponse(websocket):
    async for response in websocket:
        postEvent("t2t response generated", response)

async def sendT2TRequest(websocket, message):
    try:
        if message is not None:
            if "message" in message and "author" in message:
                await websocket.send(json.dumps(message))
            else:
                print("Invalid message format")
    except websockets.exceptions.ConnectionClosed as closedException:
            print("The T2T client has closed")
            print(closedException)
        

# async def t2tEndpoint(websocket, message: str):
#     try:
#         await websocket.send(message)
#         async for response in websocket:
#             print(f"Here is the response: {response}")
#             postEvent("t2t response generated", response)
#             # return response
#             # response = {
#             #     "response": "The websocket connection works!"
#             # }
#     except websockets.exceptions.ConnectionClosed as closedException:
#         print("The t2t client has disconnected")
#         print(closedException)