from keep_alive import keep_alive
import os
import discord
from discord.ext import commands

#------------------CONFIGS------------------
token = os.environ['TOKEN']
prefix = os.environ['prefix']


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

@bot.command()
async def load(ctx, extension):
  
  try:
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"Loaded {extension} cog!")
  except:
    await ctx.send("Cog might already be loaded!")
@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send(f"Unoaded {extension} cog!")

@bot.command()
async def reload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')
  await ctx.send("Reloaded {}".format(extension))


#------------------RUN------------------
keep_alive()
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)