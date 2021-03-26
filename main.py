import os
import discord
from discord.ext import commands

#------------------CONFIGS------------------
token = os.environ['TOKEN']
prefix = '.'
bot = commands.Bot(command_prefix=prefix)
owner = [740845704326676493, 575263293015588867]
#------------------CONFIGS------------------
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er

#------------------COMMANDS------------------

@bot.event
async def on_ready():
  print("100% loaded!")



#------------------COMMANDS------------------




#------------------RUN------------------
bot.run(token)