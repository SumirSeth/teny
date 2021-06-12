import discord
from discord.ext import commands
import os, requests, json, asyncio, random


def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
prefix = os.environ['prefix']



class Meme_Gen(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def eject(self, ctx, name:discord.Member=None, imposter=None, crew=None):
    if not name:
      await ctx.send(embed = err("Please enter a user! You can mention/user id/name/username/nickname"))
    else:
      try:
        n = name.name
        
      except:
        await ctx.send(embed = err("Please enter a user! You can mention/user id/name/username/nickname"))
      if not imposter:
        choices = ["true", "false"]
        imposter = random.choice(choices)
      
      n= n.replace(" ", "%20")
      if not crew:
        choice = ['black','blue','brown','cyan','darkgreen','lime','orange','pink','purple','red','white','yellow']
        crew = random.choice(choice)
      else:
        crew = crew.lower()
      
      
      url = f"https://vacefron.nl/api/ejected?name={n}&impostor={imposter}&crewmate={crew}"  


      await ctx.send(url)

  @commands.command()
  async def drip(self, ctx, user:discord.Member=None):
    if not user:
      await ctx.send(embed = err("Please @mention/user id/username/name/nick name is required."))
    else:
      av = user.avatar_url
      url = f"https://vacefron.nl/api/drip?user={av}"
      await asyncio.sleep(2)
      await ctx.send(url)

  @commands.command()
  async def stonks(self, ctx, user:discord.Member=None):
    if not user:
      await ctx.send(embed = err("Please @mention/user id/username/name/nick name is required."))
    else:
      av = user.avatar_url
      url = f"https://vacefron.nl/api/stonks?user={av}"
      await ctx.send(url)

  @commands.command()
  async def batman(self, ctx, u1:discord.Member=None, u2:discord.Member=None,*,arg=None):
    if not u1:
      await ctx.send(embed = err(f"Type {prefix}help batman to see command use!"))
    else:
      av1= u1.avatar_url
      av2 = u2.avatar_url
      try:
        arg = arg.split("|")
      except:
        await ctx.send(embed = err("Don't add a space after and before the |"))
      text1 = arg[0]
      text1 = text1.replace(" ", "%20")
      text2 = arg[1]
      text2 = text2.replace(" ", "%20")

      url = f"https://vacefron.nl/api/batmanslap?text1={text2}&text2={text1}&batman={av1}&robin={av2}"

      await ctx.send(url)
    
  @commands.command()
  async def carreverse(self, ctx, *, arg):
    arg = arg.replace(" ", "%20")
    url = f"https://vacefron.nl/api/carreverse?text={arg}"
    
    await ctx.send(url)

  @commands.command()
  async def changemymind(self, ctx, *, arg):
    arg = arg.replace(" ", "%20")
    url = f"https://vacefron.nl/api/changemymind?text={arg}"
    await ctx.send(url)
  
  @commands.command()
  async def firsttime(self, ctx, user:discord.Member=None):
    if not user:
      await ctx.send(embed = err("Please provide a user! @mention/user id/username/name/nickname works."))
    else:
      av = user.avatar_url
      url = f"https://vacefron.nl/api/firsttime?user={av}"
      await ctx.send(url)
    
  @commands.command()
  async def grave(self, ctx, user:discord.Member=None):
    if not user:
      await ctx.send(embed = err("Please provide a user! @mention/user id/username/name/nickname works."))
    else:
      av = user.avatar_url
      url = f"https://vacefron.nl/api/grave?user={av}"
      await ctx.send(url)

  @commands.command()
  async def trash(self, ctx, user:discord.Member=None):
    if not user:
      await ctx.send(embed = err("Please provide a user! @mention/user id/username/name/nickname works."))
    else:
      av = user.avatar_url_as(format="jpg")
      av = str(av)
      av = av[:len(av)-10]
      url = f"https://api.becoditive.xyz/v2/images/delete?image={av}"
      await ctx.send(url)
    
  @commands.command()
  async def magik(self, ctx, user:discord.Member=None, lv:int=None):
    if not user:
      await ctx.send(embed = err("Please provide a user! @mention/user id/username/name/nickname works."))
    else:
      if not lv:
        lv = 10
      av = user.avatar_url_as(format="jpg")
      url = f"https://api.devs-hub.xyz/magik?image={av}&level={lv}"
      await ctx.send(url)
  
  @commands.command()
  async def emojify(self, ctx, *,arg):
    if not arg:
      await ctx.send(embed = err("Please provide a text!"))
    else:
      arg = arg.replace(" ", "%20")
      url = f"https://api.devs-hub.xyz/emojify?text={arg}"
      data = json.loads(requests.request("GET", url=url).text)
      await ctx.send(data["emojify"])

  @commands.command()
  async def reverse(self, ctx, *, arg):
    if not arg:
      await ctx.send(embed = err("Please provide a text!"))
    else:
      arg = list(arg)
      arg.reverse()
      text = ""
      for i in arg:
        text += i
      await ctx.send(text)

  @commands.command()
  async def spank(self, ctx, u1:discord.Member=None, u2:discord.Member=None):
    if not u1:
      await ctx.send(embed = err("Please mention 2 users. @mention/user id/username/name/nickname works."))
    else:
      if not u2:
        msg = await ctx.send(embed = err("You didn't mention a 2nd user! Now the first mentioned user will be taken as the person getting spanked.\n\nThis message will be deleted in 5s."))
        await asyncio.sleep(5)
        await msg.delete()
        u1, u2= ctx.author, u1
        
      
      av1  = u1.avatar_url
      av2 = u2.avatar_url
      url = f"https://api.devs-hub.xyz/spank?face={av1}&face2={av2}"
      await ctx.send(url)
















def setup(bot):
  bot.add_cog(Meme_Gen(bot))