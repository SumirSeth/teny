import discord
from discord.ext import commands
import os
import requests, json

rkey = os.environ['rkey']
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
    url = "https://some-random-api.ml/animu/hug"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    embed = discord.Embed(title="", description=f"{ctx.message.author.name} hugs {ctx.message.mentions[0].name} 🤗", color=ctx.author.color)
    embed.set_image(url=data['link'])
    await ctx.send(embed = embed)

  @commands.command()
  async def lovecal(self, ctx, name1=None, name2=None):
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











def setup(bot):
  bot.add_cog(Fun(bot))