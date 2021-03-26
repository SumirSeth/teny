import os
import discord
from discord.ext import commands

#------------------CONFIGS------------------
token = os.environ['TOKEN']
prefix = '.'
bot = commands.Bot(command_prefix=prefix)
owner = [740845704326676493, 575263293015588867]
#------------------CONFIGS------------------


#------------------COMMANDS------------------

@bot.event
async def on_ready():
  print("100% loaded!")


#------------------COMMANDS------------------




#------------------RUN------------------
bot.run(token)