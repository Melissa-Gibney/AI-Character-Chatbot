import discord
import requests
from discord.ext import commands, voice_recv
import aiohttp
import json
import websockets

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents = intents)

apiURL = "ws://api:8080/"

generateResponse = False

async def getMessageResponse(data):
    async with websockets.connect(apiURL) as ws:
        await ws.send(json.dumps(data))
        print(f"Sent data: {json.dumps(data)}")
        response = await ws.recv()
        response = json.loads(response)
        print(f"Recieved response: {json.dumps(response)}")
        if "response" in response:
            return response["response"]
        return None

#Gets the result of the LLM by passing the message data to the Flask API
# async def getVervadaResponse(data):
#     response = requests.post(url = apiURL, json = data).json()
#     if "response" in response:
#         return response["response"]
#     print("Response not found")
#     return None

#Get a random dog image by making a request to this API
async def getRandomDogImage():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    if "message" in data:
        return data["message"]
    else:
        return None

#Print a message when the bot successfully logs in
@bot.event
async def on_ready():
    print(f'Hello world! I logged in!')

#Respond to user messages under certain conditions
@bot.event
async def on_message(message):
    if bot.user.mention in message.content and not message.mention_everyone:
        #Tell the user how to start response generation if needed
        if generateResponse:
            #Update Vervada with data on who sent the message (name, role), message contents, and other info
            author = message.author.name
            top_role = message.author.top_role.name
            channel = message.channel.name
            content = message.content.replace(bot.user.mention, "Vervada")
            data = {
                "author": author,
                "message": content,
                "inVoiceChat": False
            }
            #Get a response from Vervada
            response = await getMessageResponse(data) #await getVervadaResponse(data)
            if not response:
                await message.channel.send("I couldn't get my API response :(")
            else:
                await message.channel.send(response)
        else:
            await message.channel.send("Type !toggleResponseGeneration to let me respond to messages")
    await bot.process_commands(message)

#Toggles whether the bot will generate a response when @-ed
@bot.command()
async def toggleResponseGeneration(ctx):
    global generateResponse
    if not generateResponse:
        await ctx.send("You can now get responses by @-ing my username! Type @Vervada anywhere in your message to get a response")
        generateResponse = True
    else:
        generateResponse = False
        await ctx.send("I will no longer to your messages if you @ me.")

#Command for getting random dog images
#This was originally a test for retrieving data over HTTP
@bot.command()
async def dog(ctx):
    dogImage = await getRandomDogImage()
    if not dogImage:
        await ctx.send("I couldn't get a dog image :(")
    else:
        embed = discord.Embed(title="Random Dog Image")
        embed.set_image(url=dogImage)
        await ctx.send(embed = embed)

#Listens to a voice channel and prints whether the user is speaking
#WIP to be used for STT purposes
@bot.command()
async def record(ctx):
    def callback(user, data: voice_recv.VoiceData):

        packet = data.packet

        if(packet.is_silence()):
            print(f"{user} is silent")
        else:
            print(f"{user} is making noise")

    voice = ctx.author.voice

    if not voice:
        await ctx.send("⚠️ You aren't in a voice channel!")
    else:
        vc = await voice.channel.connect(cls=voice_recv.VoiceRecvClient)
        vc.listen(voice_recv.BasicSink(callback))
        await ctx.send("🔴 Listening to this conversation.")

with open("discord_secret.json", "r") as secretFile:
  secret = json.load(secretFile)

key = secret["bot_ref"]
  
print(key)

bot.run(key)