from event import subscribe
import asyncio
from Endpoints.t2t_ep import sendT2TRequest
from Endpoints.discord_ep import sendResponse

def handleDiscordMessageRecieved(data):
    print("Handling discord message")
    asyncio.create_task(sendResponse(data[0], f"This was your message: {data[1]["message"]}"))
    #sendT2TRequest(data) TODO hookup T2T
    
def setupT2TListener():
    subscribe("discord message recieved", handleDiscordMessageRecieved)