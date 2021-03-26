from keep_alive import keep_alive
import os
import discord
from discord.ext import commands

#------------------CONFIGS------------------
token = os.environ['TOKEN']
prefix = '.'
bot = commands.Bot(command_prefix=prefix, help_command=None)
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
@bot.group(invoke_without_command=True)
async def help(ctx):
  e = discord.Embed(title="Help", description=f"Type {prefix}help <command> for more info.", color=ctx.author.color)
  e.add_field(name="General", value=f"{prefix}fact", inline=True)
  await ctx.send(embed=e)
@help.command()
async def fact(ctx):
  e = discord.Embed(title="Fact!", description="Gives a random fact each time!", color=ctx.author.color)
  e.add_field(name="**Syntax**", value=f"`{prefix}fact`")
  await ctx.send(embed=e)



#------------------RUN------------------
keep_alive()
bot.run(token)