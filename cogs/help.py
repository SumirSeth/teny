import discord
from discord.ext import commands
import os

prefix = os.environ['prefix']
class Help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("Cog ready!")
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="spookie"))


  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    e = discord.Embed(title="Help", description=f"Type {prefix}help <command> for more info.", color=ctx.author.color)
    e.add_field(name="Fact", value=f"`cat`, `anime`, `useless`, `chuck`, `num`, `dog`", inline=True)
    e.add_field(name="Info", value=f"`{prefix}country <name>`, `{prefix}weather <place>`", inline=False)
    e.add_field(name="Fun", value=f"`{prefix}hug <user>`, `{prefix}lovecal <name 1> <name 2>`", inline=False)
    await ctx.send(embed=e)


  @help.command()
  async def fact(self, ctx):
    e = discord.Embed(title="Fact!", description=f"A category filled with various types of facts!\nType {prefix}fact for more info.", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}fact <category>`")
    await ctx.send(embed=e)

  @help.command()
  async def country(self, ctx):
    e = discord.Embed(title="Country!", description=f"Get any countries info!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}country <name>`")
    await ctx.send(embed=e)
  @help.command()
  async def weather(self, ctx):
    e = discord.Embed(title="Weather!", description=f"Get any place's weather info!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}weather <place>`")
    await ctx.send(embed=e)
  @help.command()
  async def hug(self, ctx):
    e = discord.Embed(title="Hug!", description=f"Hug anyone!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}hug <user>`")
    await ctx.send(embed=e)
  @help.command()
  async def lovecal(self, ctx):
    e = discord.Embed(title="Love Calculator!", description=f"Calculate love % between 2 people!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}lovecal <name 1> <name 2>`")
    await ctx.send(embed=e)



def setup(bot):
  bot.add_cog(Help(bot))