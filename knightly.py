import discord
from dotenv import load_dotenv
import os

#load config
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')
TEST_SERVER_ID = os.getenv('TEST_SERVER_ID')
ADMIN_ROLE = os.getenv('ADMIN_ROLE')
OFFICER_ROLE = os.getenv('OFFICER_ROLE')
KNIGHT_ROLE = os.getenv('KNIGHT_ROLE')
RECRUIT_ROLE = os.getenv('RECRUIT_ROLE')
LFG_CHANNEL = 1222001635589357728

# sql server connection details

#connect to discord
#set intents
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

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

@bot_client.event
async def on_presence_update(before, after):
    try:
        print (f'Presence change: {after.activity.name}')
        lfg_channel = bot_client.get_channel(LFG_CHANNEL)
        await lfg_channel.send(f'{after.name} is now playing {after.activity.name}')
    except:
        print ('Stopped Playing')

#start up server w/ bot_token using environmental token 
bot_client.run(BOT_TOKEN)