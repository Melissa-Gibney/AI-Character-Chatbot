# from flask import Flask, jsonify, url_for
# from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
#from T2T import t2t
#from STT import stt
from Endpoints import discord_ep, t2t_ep
from connection_manager import ConnectionManager
# import uvicorn
import asyncio
import websockets
from Listeners.log_listener import setupLogListener
from Listeners.t2t_listener import setupT2TListener

# manager = ConnectionManager()

# @app.websocket("/api/discord/message")
# async def discordEndpoint(websocket: WebSocket):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             data = json.loads(data)
#             #TODO: emit messages saying I recieved data
#             print(f"I recieved data: {json.dumps(data)}")
#             #TODO: get response from T2T
#             response = {
#                 "response": "The websocket connection works!"
#             }
#             await websocket.send_text(json.dumps(response))
#             #manager.sendJSON(response)
#             print(f"I sent my response: {json.dumps(response)}")
#     except WebSocketDisconnect:
#         print("The discord message websocket was closed")

async def discordLoop():
    discordServer = await websockets.serve(discord_ep.messageEndpoint, host="0.0.0.0", port=8080)
    await discordServer.serve_forever()

async def t2tLoop():
    t2tServer = await websockets.serve(t2t_ep.t2tEndpoint, host="0.0.0.0", port=8081)
    await t2tServer.serve_forever()

if __name__ == "__main__":
    setupLogListener()
    setupT2TListener()
    asyncio.run(discordLoop())
    asyncio.run(t2tLoop())