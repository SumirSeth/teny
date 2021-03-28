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
    e.add_field(name="Info", value=f"`{prefix}country <name>`, `{prefix}weather <place>`, `{prefix}news <search term> <page number>`, `{prefix}covid <country name>`, `{prefix}urban <search term>`", inline=False)
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
  @help.command()
  async def news(self, ctx):
    e = discord.Embed(title="News!", description=f"Get the breaking news for any search term!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}news <search term> <page number>`")
    e.add_field(name="Example", value=f"`{prefix}news Elon Musk 1`\nWhere 'Elon Musk' is the search term and '1' is the result page number!")
    await ctx.send(embed=e)
  @help.command()
  async def covid(self, ctx):
    e = discord.Embed(title="Covid!", description=f"Get the covid stats for any country!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}covid <country name>`")
    await ctx.send(embed=e)
  @help.command()
  async def urban(self, ctx):
    e = discord.Embed(title="Urban Dictionary!", description=f"Get definition of any word from urban dictionary!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}urban <search term>`")
    await ctx.send(embed=e)



def setup(bot):
  bot.add_cog(Help(bot))