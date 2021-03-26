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

  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    e = discord.Embed(title="Help", description=f"Type {prefix}help <command> for more info.", color=ctx.author.color)
    e.add_field(name="General", value=f"{prefix}fact", inline=True)
    await ctx.send(embed=e)
  @help.command()
  async def fact(self, ctx):
    e = discord.Embed(title="Fact!", description="Gives a random fact each time!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}fact`")
    await ctx.send(embed=e)




def setup(bot):
  bot.add_cog(Help(bot))