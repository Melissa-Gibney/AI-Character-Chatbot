import websockets
class ConnectionManager:
    def __init__(self):
        self.active_connections: list = []

    async def connect(self, websocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket):
        self.active_connections.remove(websocket)
        await websocket.close()

    async def sendJSON(self, data: str, websocket):
        await websocket.send_json(data)

    async def sendText(self, data: str, websocket):
        await websocket.send_text(data)

    async def send_personal_message(self, message: str, websocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)