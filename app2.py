#https://discordapp.com/oauth2/authorize?&client_id=978315488260128838&scope=bot&perms=8

import discord
from discord.ext import commands
import music
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("discord_token")

cogs = [music]

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run(DISCORD_TOKEN)


