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

bot_client = discord.Client(intents=intents)
#fire off client using environmental token 
bot_client.run(BOT_TOKEN)