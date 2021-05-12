import discord
from discord.ext import commands
import os
import requests, json, string, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime
import urllib.parse
import alexflipnote
import time, asyncio

alex = alexflipnote.Client("A4r4T7opKWOTnLnwOXDLYKLnlEkvi2cbgkIMTci5")

rkey = os.environ['rkey']
def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
prefix = os.environ['prefix']

class Fun(commands.Cog):


  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hug(self, ctx, arg=None):
    try:
      url = "https://some-random-api.ml/animu/hug"
      response = requests.request("GET", url)
      data = json.loads(response.text)
      if not arg:
        embed = discord.Embed(title="", description=f"🤗", color=ctx.author.color)
        embed.set_image(url=data['link'])
      else:
        embed = discord.Embed(title="", description=f"{ctx.message.author.name} hugs {ctx.message.mentions[0].name} 🤗", color=ctx.author.color)
        embed.set_image(url=data['link'])
      await ctx.send(embed = embed)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command()
  async def wink(self, ctx, arg=None):
    try:
      url = "https://some-random-api.ml/animu/wink"
      response = requests.request("GET", url)
      data = json.loads(response.text)
      if not arg:
        embed = discord.Embed(title="", description=f"😉", color=ctx.author.color)
        embed.set_image(url=data['link'])
      else:
        embed = discord.Embed(title="", description=f"{ctx.message.author.name} winks {ctx.message.mentions[0].name} 😉", color=ctx.author.color)
        embed.set_image(url=data['link'])
      await ctx.send(embed = embed)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command()
  async def lovecal(self, ctx, name1=None, name2=None):
    try:
      if not name1 or not name2:
        if not name1:
          await ctx.send(embed=err("Enter 2 names!"))
        else:
          await ctx.send(embed=err("Enter the second name!"))
      else:
        url = "https://love-calculator.p.rapidapi.com/getPercentage"
        querystring = {"fname": name1, "sname": name2}

        headers = {
            'x-rapidapi-key': f"{rkey}",
            'x-rapidapi-host': "love-calculator.p.rapidapi.com"
        }

        response = requests.request("GET",url,
                                    headers=headers,
                                    params=querystring)
        json_data = json.loads(response.text)
        
        em = discord.Embed(title="Love Calculator!", description=f'First Person: **{json_data["fname"]}**\nSecond Person: **{json_data["sname"]}**\nLove %: **{json_data["percentage"]}%**\nLove FeedBack: **{json_data["result"]}**', color=ctx.author.color)
        await ctx.send(embed=em)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command()
  async def advice(self, ctx):
    try:
      url = "https://api.adviceslip.com/advice"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)

      em = discord.Embed(title="Advice for you!", description=data["slip"]["advice"], color= ctx.author.color)
      await ctx.send(embed=em)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  @commands.command()
  async def bill(self, ctx):
    try:
      def m():
        num = random.randint(1,5)
        l = string.ascii_letters
        u = string.digits
        o = ( ''.join(random.choice(l) for i in range(num)) )
        n = ( ''.join(random.choice(u) for i in range(num)) )
        b = str(o+n)
        return b



      url = f"https://belikebill.ga/billgen-API.php?default=1{m()}"
      e = discord.Embed(title="Be like bill", color=ctx.author.color, url=url)
      e.set_image(url=url)
      await ctx.send(embed=e)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command()
  async def kanye(self, ctx):
    try:
      url = "https://api.kanye.rest/"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      embed = discord.Embed(title="Kanye West Quotes!", color=ctx.author.color, description=data["quote"])
      await ctx.send(embed=embed)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command()
  async def gay(self, ctx, member:discord.Member=None):
    try:
      if not member:
        embed = discord.Embed(title="Gay Rate!", description=f"🏳️‍🌈 {ctx.author.name} is {random.randint(1,100)}% gay. 🏳️‍🌈", color=ctx.author.color)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title="Gay Rate!", description=f"🏳️‍🌈 {member.name} is {random.randint(1,100)}% gay. 🏳️‍🌈", color=ctx.author.color)
        await ctx.send(embed=embed)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @commands.command()
  async def pp(self, ctx, member:discord.Member=None):
    try:
      if not member:
        embed = discord.Embed(title="PP Size!", description=f" {ctx.author.name}'s pp is {round(random.uniform(1,10), 2)} inches long.", color=ctx.author.color)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title="PP Size!", description=f" {member.name}'s pp is {round(random.uniform(1,10), 2)} inches long.", color=ctx.author.color)
        await ctx.send(embed=embed)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command()
  async def quote(self, ctx):
    try:
      response = requests.request("GET", url="https://zenquotes.io/api/random")
      data = json.loads(response.text)
      
      o = f'**"{data[0]["q"]}"**\n\n-{data[0]["a"]}'
      await ctx.send(embed=em(ctx,"Random Quotes!",o))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
    
  @commands.command()
  async def meme(self, ctx):
    try:
      response = requests.request("GET", url="https://meme-api.herokuapp.com/gimme")
      data = json.loads(response.text)
      emb = em(ctx, "Meme for You!", f'[{data["title"]}]({data["postLink"]})')
      emb.set_image(url=data["url"])
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.channel.id == 836263071701794847:
      def c(arg, e):
          a = e
          b = ''
          for i in range(int(arg)):
            b = a+b
          return b
      if message.author.id == 533257402267598868:
        n = random.randint(1, 70)
        await message.channel.send(f"Stoof clowned {c(n, '🤡')}\n\nClowns: {n}")
      elif message.author.id == 471687158239854594:
        n = random.randint(1, 70)
        #await message.channel.send(f"Hunter big brain {c(n, '🧠')}\n\nBrains: {n}")
        await message.channel.send(message.content)
      elif message.author.id == 575263293015588867:
        n = random.randint(1, 70)
        await message.channel.send(message.content)

  @commands.command()
  async def monke(self,ctx):
    try:
      def m():
        num = random.randint(1,5)
        l = string.ascii_letters
        u = string.digits
        o = ( ''.join(random.choice(l) for i in range(num)) )
        n = ( ''.join(random.choice(u) for i in range(num)) )
        b = str(o+n)
        return b
      emb = em(ctx, "Reject Humanity, return to Monke",'')
      emb.set_image(url=f'https://www.placemonkeys.com/500/350?random={m()}')
      await ctx.send(embed=emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command(aliases=["8ball", "8Ball"])
  async def eightball(self, ctx, * , arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please give a question!"))
      else:
        responses =  ["As I see it, yes.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don’t count on it.","It is certain.","It is decidedly so.","Most likely.","My reply is no.","My sources say no.","Outlook not so good.","Outlook good.","Reply hazy, try again.","Signs point to yes.","Very doubtful.","Without a doubt.","Yes.","Yes – definitely.","You may rely on it."]
        r = random.choice(responses)
        desc = f'*Question*: **{arg}**\n\n*Answer*: **{r}**'
        await ctx.send(embed = em(ctx, "8 Ball!", desc))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @commands.command()
  async def doge(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("No arguments given."))
      else:
        arg = urllib.parse.quote_plus(arg)
        url = f"https://api.funtranslations.com/translate/doge.json?text={arg}"
        response = requests.request("GET", url=url)
        data = json.loads(response.text)
        tran = data["contents"]["translated"]
        tex = data["contents"]["text"]
        desc = f"*Text*: **{tex}**\n\n*Doge Language:* **{tran}**"
        await ctx.send(embed= em(ctx, "Doge Translations!", desc))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @commands.command()
  async def aff(self, ctx):
    try:
      url = "https://www.affirmations.dev/"
      response = requests.request("GET", url=url)
      data = json.loads(response.text)
      af = data["affirmation"]
      await ctx.send(embed = em(ctx, "Affirmation from Tény!",af))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @commands.command(aliases=["y/n"])
  async def yesno(self, ctx, arg):
    try:
      if not arg:
        await ctx.send(embed = err("You forgot to give a question."))
      else:
        url = "https://yesno.wtf/api/"
        response = requests.request("GET", url=url)
        data = json.loads(response.text)
        a = data["answer"]
        l = data["image"]
        embed = em(ctx, "Yes or No-", f'**{a}**')
        embed.set_image(url = l)
        await ctx.send(embed = embed)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()









def setup(bot):
  bot.add_cog(Fun(bot))