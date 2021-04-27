import discord
from discord.ext import commands
import os
import requests, json
import traceback

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
    e.add_field(name="Available choices:", value="cat, anime, useless, chuck, num, dog")
    e.add_field(name="Syntax:", value=f"`{prefix}fact <category>`\nEg: '{prefix}fact cat'")
    await ctx.send(embed=e)

  @fact.command()
  async def cat(self, ctx):
    try:
      url = "https://catfact.ninja/fact?max_length=500"
      response = requests.request("GET", url)
      data = json.loads(response.text)
      await ctx.send(embed=em(ctx, "Cat fact!", data["fact"]))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @fact.command()
  async def anime(self, ctx):
    try:
      url = "https://animu.p.rapidapi.com/fact"
      headers = {
          'x-rapidapi-key': "e123529625msh5f98aa5bd893b45p1df177jsn008200ae5772",
          'x-rapidapi-host': "animu.p.rapidapi.com"
          }
      response = requests.request("GET", url, headers=headers)
      data = json.loads(response.text)
      #await ctx.send(data)
      await ctx.send(embed=em(ctx, "Anime fact!", data["fact"]))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @fact.command()
  async def useless(self, ctx):
    try:
      url = "https://useless-facts.sameerkumar.website/api"
      response = requests.request("GET", url)
      data = json.loads(response.text)
      await ctx.send(embed=em(ctx,"Useless fact!", data["data"]))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @fact.command()
  async def chuck(self, ctx):
    try:
      url = "https://api.chucknorris.io/jokes/random"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      await ctx.send(embed=em(ctx, "Chuck Norris fact!", data["value"]))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @fact.command()
  async def num(self, ctx, arg=''):
    try:
      try:
        if isinstance(int(arg), int):    
          url = f"http://numbersapi.com/{arg}"
      except:
        url= "http://numbersapi.com/random"
      response = requests.request("GET", url=url)
      await ctx.send(embed=em(ctx, "Number fact!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @fact.command()
  async def dog(self, ctx):
    try:
      url = "https://dog-api.kinduff.com/api/facts"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      await ctx.send(embed=em(ctx, "Dog Fact!", data["facts"][0]))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
    






def setup(bot):
  bot.add_cog(Fact(bot))