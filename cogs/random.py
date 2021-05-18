import discord
from discord.ext import commands
import os, requests, json, random
import alexflipnote
import asyncio

alex = alexflipnote.Client("A4r4T7opKWOTnLnwOXDLYKLnlEkvi2cbgkIMTci5")


def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
prefix = os.environ['prefix']



class Random(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.group(invoke_without_command=True)
  async def random(self, ctx):
    pass
  
  @random.command()
  async def cat(self, ctx):
    try:
      url = "https://api.thecatapi.com/v1/images/search"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      cat = data[0]["url"]
      emb = em(ctx, "Random Cat Images!",'')
      emb.set_image(url=cat)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @random.command()
  async def dog(self, ctx):
    try:
      url = "https://dog.ceo/api/breeds/image/random"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      dog = data["message"]
      emb = em(ctx, "Random Dog Images!",'')
      emb.set_image(url=dog)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @random.command()
  async def fox(self, ctx):
    try:
      url = "https://randomfox.ca/floof/"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      fox = data["image"]
      emb = em(ctx, "Random Fox Images!",'')
      emb.set_image(url=fox)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @random.command()
  async def panda(self, ctx):
    try:
      url = "https://some-random-api.ml/img/panda"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      panda = data["link"]
      emb = em(ctx, "Random Panda Images!",'')
      emb.set_image(url=panda)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @random.command()
  async def redpanda(self, ctx):
    try:
      url = "https://some-random-api.ml/img/red_panda"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      rpanda = data["link"]
      emb = em(ctx, "Random Red Panda Images!",'')
      emb.set_image(url=rpanda)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @random.command()
  async def bird(self, ctx):
    try:
      url = "https://some-random-api.ml/img/birb"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      bird = data["link"]
      emb = em(ctx, "Random Bird Images!",'')
      emb.set_image(url=bird)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @random.command()
  async def koala(self, ctx):
    try:
      url = "https://some-random-api.ml/img/koala"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      koala = data["link"]
      emb = em(ctx, "Random Koala Images!",'')
      emb.set_image(url=koala)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @random.command()
  async def image(self, ctx):
    try:
      url = f"https://source.unsplash.com/random/300x200?sig=${random.randint(1, 100000)}"
      emb = em(ctx, "Random Images!",'')
      emb.set_image(url=url)
      await ctx.send(embed = emb)  
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @random.command()
  async def color(self, ctx):
    try:
      url = "https://random-data-api.com/api/color/random_color"
      
      response = requests.request("GET", url=url)
      
      data = json.loads(response.text)
      a = data["hex_value"]
      he = a
  
      img = await alex.colour_image(colour = a)
      a = a[1:]
      
      brl = f"http://thecolorapi.com/id?hex={a}"
      a = int(a, 16)
      a = hex(a)
      a = int(a, 16)
      res = requests.request("GET", url = brl)
      await asyncio.sleep(3)
      d = json.loads(res.text)
      name = d["name"]["value"]
      emb = discord.Embed(title="Random Color!", description=f"*Name*: **{name}**\n\n*Hex*: **{he}**", color = a)
      
      emb.set_thumbnail(url = img)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @random.command()
  async def waifu(self, ctx):
    url = f"https://www.thiswaifudoesnotexist.net/example-{random.randint(1,100000)}.jpg"

    await ctx.send(embed = em(ctx, "Waifu!", "").set_image(url=url))
  
  






























def setup(bot):
  bot.add_cog(Random(bot))