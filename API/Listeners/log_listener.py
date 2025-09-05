from event import subscribe

def handleDiscordMessageRecieved(data):
    if "message" in data[1] and "author" in data[1]:
        print(f"Discord Message Recieved - {data[1]["author"]}: {data[1]["message"]}")
    else:
        print(f"Discord Message Recieved - INVALID MESSAGE FORMAT")

def handleT2TResponseGenerated(data):
    if "response" in data:
        print(f"T2T Response Recieved - Vervada: {data["response"]}")
    else:
        print(f"T2T Response Recieved - INVALID RESPONSE FORMAT")
    
def setupLogListener():
    subscribe("discord message recieved", handleDiscordMessageRecieved)
    subscribe("t2t response generated", handleT2TResponseGenerated)