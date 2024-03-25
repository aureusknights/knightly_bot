import discord
from dotenv import load_dotenv
import os

#load config
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
# sql server connection details

#connect to discord
#set intents
intents = discord.Intents.default()
intents.message_content = True

bot_client = discord.Client(intents=intents)

# register events
@bot_client.event
async def on_ready():
    print(f'Logged in as {bot_client.user}')

@bot_client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

    if message.content.startswith('Ping?'):
        await message.channel.send('Pong!')

#start up server w/ bot_token using environmental token 
bot_client.run(BOT_TOKEN)