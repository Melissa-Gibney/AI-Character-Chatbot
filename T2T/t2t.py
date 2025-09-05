import asyncio
import json
import open_ai_model
import websockets

def createPrompt(message, author):# context):
        return f"{author} says: {message}\nVervada says: "

def getOpenAIOutput(message, author, context):
    open_ai_model.userRequest = createPrompt(message, author)
    return open_ai_model.getCompletion()

async def getT2TResponse(apiURL):
    async with websockets.connect(apiURL) as ws:
        message = await ws.recv()
        message = json.loads(message)
        print(f"Recieved message: {json.dumps(message)}")
        if "message" in message and "author" in message:
            return await getOpenAIOutput(message["message"], message["author"])
        return None

if __name__ == "__main__":
    asyncio.run(getT2TResponse("ws://api:8081/"))