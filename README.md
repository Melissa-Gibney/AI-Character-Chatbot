Before getting into how to setup the system for my bot I'll get into the specifics of what code I pulled from while setting up both the frontend discord bot and backend API.

For the discord bot, I referenced the discord.py quickstart (https://discordpy.readthedocs.io/en/stable/quickstart.html) and API documentation (https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#), along with the voice recv extension example script on its github (https://github.com/imayhaveborkedit/discord-ext-voice-recv/blob/main/examples/recv.py). I pulled part of the voice recv example script to simply use the basic sink and callback inside of my record command and it only prints whether the user is speaking or not.  As I was figuring out how to get information from an API, I also found this video explaining how to get random images from a dog image database using this tutorial: https://www.youtube.com/watch?v=nqe9FgRVlPA&t=136s. I kept the command for getting images of dogs in my own bot, and once I understood it, I adapted it to create the function for post requests to my own API.  The rest of the discord bot was coded from scratch while referencing the documentation mentioned previously.

As for the backend API, I referenced this YouTube tutorial and pulled out the sections that were relevant to creating the get, post, and put requests for my own API endpoint for Discord: https://www.youtube.com/watch?v=z3YMz-Gocmw&t=1246s. I altered sections involving the fields, arguments, and respource to fit with what I needed for passing information to and from the discord endpoint. In the end, I only used POST requests to send messages between Discord and the API endpoint.

The T2T file is made of entirely original code, and the open_ai_model file is taken partially from the OpenAI API documentation (https://platform.openai.com/docs/guides/text?api-mode=responses). I essentially put the call to generate the LLM output inside of a function and called it from the T2T file.

Aside from the boilerplate code created when setting up the React app, the rest of the code is original. If you have any further questions on how I utilized these resources, please feel free to ask me.

In order to run the discord bot with its LLM backend, you will need four things before beginning:
1. Your own discord account
2. A discord server, preferably your own, where you can invite the bot to join
3. A discord developer application
4. A ChatGPT API key and enough credits to handle the generations you make with the bot

You can easily sign up for your own discord account, and after that, you can create your own server by going to the "Add Server" button in the bottom left of the site and choosing the option to create your own server.  To create the discord development application, go to https://discord.com/developers/applications and choose the option to create your own application.  Name it however you want and go into the Bot tab of the application to set up its permissions.  When you first create the bot, you are given a Token.  Copy and paste this token into line 109 of bot-main.py to replace the current one.  Back in the bot creation window, make sure you enable administrative permissions and turn on all privilaged gateway intents.  That should be all that is needed to set up the bot online.  If you are having trouble, please reference the part of the video where I show you my bot's settings or email me with any questions.  After that, your bot can be invited to a discord server by creating a link that looks like this with the correct client ID, permissions, and scope: https://discord.com/api/oauth2/authorize?client_id=YOURCLIENTID&permissions=8&scope=YOURSCOPE.  Permissions = 8 gives the bot administrator permissions, and you should ensure that the scope includes bot, guilds.members.read, applications.commands, and messages.read.

Now that the bot is set up, here are all of the Python libraries that you should need to install for both the frontend and the backend code to run:
aiohttp==3.11.12
discord-ext-voice-recv==0.4.2a145
discord.py==2.4.0
Flask==3.1.0
flask-cors==5.0.1
Flask-RESTful==0.3.10
openai==1.63.2
openai-whisper==20240930
PyNaCl==1.5.0

discord.py should be installed using discord.py[voice] to install PyNaCl and ensure that it works with the voice-recv extension. You must install this specific version of discord.py in order for it to work with the voice-recv extension. If you run into any issues with installation, please let me know and I am happy to help with troubleshooting. The documentation for each of these libraries can be found at: https://pypi.org/. I installed all of these using the "python3 -m pip install" command because I am on a MacBook Pro.

In addition to Python and Flask, the vervada-react-tsx folder in this project does have other dependencies (namely react and vue), but that website is currently not used for anything relating to the project.  You should not need to run the website, but if you decide to do so for some reason, you should ensure you can run React applications involving Typescript and Vue.  I am leaving it in because I plan to use it to monitor each part of the application individually in the future (namely, monitoring the LLM output before it passes into the future TTS module and adjusting filters for the LLM output). 

In case I forgot a required library in that previous list, here are all of the libraries returned when I run "pip freeze" from within this project:
aiohappyeyeballs==2.4.6
aiohttp==3.11.12
aiosignal==1.3.2
aniso8601==10.0.0
annotated-types==0.7.0
anyio==4.8.0
attrs==25.1.0
blinker==1.9.0
certifi==2025.1.31
cffi==1.17.1
charset-normalizer==3.4.1
click==8.1.8
discord-ext-voice-recv==0.4.2a145
discord.py==2.4.0
distro==1.9.0
filelock==3.18.0
Flask==3.1.0
flask-cors==5.0.1
Flask-RESTful==0.3.10
frozenlist==1.5.0
fsspec==2025.3.2
h11==0.14.0
httpcore==1.0.7
httpx==0.28.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.6
jiter==0.8.2
llvmlite==0.44.0
MarkupSafe==3.0.2
more-itertools==10.7.0
mpmath==1.3.0
multidict==6.1.0
networkx==3.4.2
numba==0.61.2
numpy==2.2.5
openai==1.63.2
openai-whisper==20240930
propcache==0.3.0
pycparser==2.22
pydantic==2.10.6
pydantic_core==2.27.2
PyNaCl==1.5.0
pytz==2025.2
regex==2024.11.6
requests==2.32.3
six==1.17.0
sniffio==1.3.1
sympy==1.13.3
tiktoken==0.9.0
torch==2.2.2
tqdm==4.67.1
typing_extensions==4.12.2
urllib3==2.4.0
Werkzeug==3.1.3
yarl==1.18.3