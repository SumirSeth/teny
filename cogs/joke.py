import discord
from discord.ext import commands
import os, requests, json, asyncio


def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
prefix = os.environ['prefix']

class Joke(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True)
  async def joke(self, ctx):
    e = discord.Embed(title="Joke!", description="A sub-category that contains different types of jokes.", color=ctx.author.color)
    e.add_field(name="Categories:", value=f"Programming (pro), Miscellaneous (misc), Dark (d), Pun (p), Spooky (sp), Christmas (chr), Dadjoke(dad), yomom, bread\n\nFor random fact use `{prefix}joke any`\n ")
    e.add_field(name="Syntax:", value=f'{prefix}joke <category name>', inline=False)
    e.add_field(name="Example:",value=f'For random jokes use: `{prefix}joke any`.\nFor a category type `{prefix}joke <category name>`\nEg: `{prefix}joke pro` for programming jokes.')
    await ctx.send(embed=e)
  @joke.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def any(self, ctx):
    try:
      url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)

      cat = data["type"]
      if cat == "singe":
        joke = data["joke"]
        await ctx.send(embed=em(ctx, "Random Joke!", joke))
      elif cat == "twopart":
        setup = data["setup"]
        delivery = data["delivery"]
        await ctx.send(embed=em(ctx, "Randome Joke!",f'{setup}\n\n---> {delivery}'))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @any.error
  async def any_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
          await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s."))
      else:
          raise error

  @joke.command(aliases=['pro'])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def programming(self, ctx):
    try:
      url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt"
      response = requests.request("GET", url=url)
      await ctx.send(embed = em(ctx, "Programming Jokes!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @programming.error
  async def programming_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s."))
    else:
      raise error

  @joke.command(aliases=['misc'])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def miscellaneous(self, ctx):
    try:
      url = "https://v2.jokeapi.dev/joke/Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt"
      response = requests.request("GET", url=url)
      await ctx.send(embed = em(ctx, "Miscellaneous Jokes!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @miscellaneous.error
  async def miscellaneous_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s."))
    else:
      raise error
  
  @joke.command(aliases=['d'])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def dark(self, ctx):
    try:
      url = "https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt"
      response = requests.request("GET", url=url)
      await ctx.send(embed = em(ctx, "Dark Jokes!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @dark.error
  async def dark_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s."))
    else:
      raise error
  
  @joke.command(aliases=['p'])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def pun(self, ctx):
    try:
      url = "https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt"
      response = requests.request("GET", url=url)
      await ctx.send(embed = em(ctx, "Puns!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @pun.error
  async def pun_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s."))
    else:
      raise error

  @joke.command(aliases=['sp'])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def spooky(self, ctx):
    try:
      url = "https://v2.jokeapi.dev/joke/Spooky?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt"
      response = requests.request("GET", url=url)
      await ctx.send(embed = em(ctx, "Spooky Jokes!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @spooky.error
  async def spooky_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s."))
    else:
      raise error

  @joke.command(aliases=['chr'])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def christmas(self, ctx):
    try:
      url = "https://v2.jokeapi.dev/joke/Dark?blacklistFlags=nsfw,religious,political,racist,sexist&format=txt"
      response = requests.request("GET", url=url)
      await ctx.send(embed = em(ctx, "Christmas Jokes!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @christmas.error
  async def christmas_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s."))
    else:
      raise error

  @joke.command(aliases=['dad'])
  @commands.cooldown(1,10, commands.BucketType.user)
  async def dadjoke(self, ctx):
    try:
      headers = {
          'Accept': 'text/plain',
      }

      response = requests.get('https://icanhazdadjoke.com/', headers=headers)
      await ctx.send(embed=em(ctx, "Dad Jokes!", response.text))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @dadjoke.error
  async def dadjoke_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s"))
    else:
      raise error
  
  @joke.command()
  @commands.cooldown(1,10, commands.BucketType.user)
  async def yomom(self, ctx):
    try:
      url = "https://api.yomomma.info/"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      mam = data["joke"]
      await ctx.send(embed  = em(ctx, "Yo momma!", mam))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @yomom.error
  async def yomom_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s"))
    else:
      raise error
      
  @joke.command()
  @commands.cooldown(1,10, commands.BucketType.user)
  async def bread(self, ctx):
    try:
      url = "https://my-bao-server.herokuapp.com/api/breadpuns"
      response = requests.request("GET", url=url)
      
      b = response.text
      await ctx.send(embed  = em(ctx, "Bread Puns!", b))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @bread.error
  async def bread_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(embed=err("This command is on cooldown. Cooldown time: 10s"))
    else:
      raise error

    






















def setup(bot):
  bot.add_cog(Joke(bot))