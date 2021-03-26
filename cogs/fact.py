import discord
from discord.ext import commands
import os
import requests, json

def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
prefix = os.environ['prefix']
class Fact(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.group(invoke_without_command=True)
  async def fact(self, ctx):
    e = discord.Embed(title="Fact!", description="Get various types of facts with this command!", color = ctx.author.color)
    e.add_field(name="Available choices:", value="cat, anime, useless, chuck, num")
    e.add_field(name="Syntax:", value=f"`{prefix}fact <category>`\nEg: '{prefix}fact cat'")
    await ctx.send(embed=e)

  @fact.command()
  async def cat(self, ctx):
    url = "https://catfact.ninja/fact?max_length=500"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    await ctx.send(embed=em(ctx, "Cat fact!", data["fact"]))

  @fact.command()
  async def anime(self, ctx):
    url = "https://animu.p.rapidapi.com/fact"
    headers = {
        'x-rapidapi-key': "e123529625msh5f98aa5bd893b45p1df177jsn008200ae5772",
        'x-rapidapi-host': "animu.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    await ctx.send(embed=em(ctx, "Anime fact!", data["fact"]))
  
  @fact.command()
  async def useless(self, ctx):
    url = "https://useless-facts.sameerkumar.website/api"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    await ctx.send(embed=em(ctx,"Useless fact!", data["data"]))

  @fact.command()
  async def chuck(self, ctx):
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.request("GET", url=url)
    data = json.loads(response.text)
    await ctx.send(embed=em(ctx, "Chuck Norris fact!", data["value"]))
  
  @fact.command()
  async def num(self, ctx, arg=''):
    try:
      if isinstance(int(arg), int):    
        url = f"http://numbersapi.com/{arg}"
    except:
      url= "http://numbersapi.com/random"
    response = requests.request("GET", url=url)
    await ctx.send(embed=em(ctx, "Number fact!", response.text))
    






def setup(bot):
  bot.add_cog(Fact(bot))