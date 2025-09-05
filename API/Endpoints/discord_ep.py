import asyncio
import json
from connection_manager import ConnectionManager
import websockets
from event import postEvent, subscribe

#Closing the websocket delays the discord bot response?
async def messageEndpoint(websocket):
    recieveMessageTask = asyncio.create_task(recieveMessage(websocket))
    sendResponseTask = asyncio.create_task(sendResponse(websocket, None))
    done, pending = await asyncio.wait(
        [recieveMessageTask, sendResponseTask])
    for task in pending:
        print(task)
        task.cancel()

# Logic for sending a message after recieving it from the discord bot
async def recieveMessage(websocket):
    async for message in websocket:
        postEvent("discord message recieved", [websocket, json.loads(message)])

async def sendResponse(websocket, response):
    try:
        if response is not None:
            response = {
                "response": response
            }
            await websocket.send(json.dumps(response))
    except websockets.exceptions.ConnectionClosed as closedException:
            print("The discord client has closed")
            print(closedException)
        
        

# def setupDiscordHandler():
#     subscribe("t2t response generated", sendResponse)