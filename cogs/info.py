import discord
from discord.ext import commands
import os
import requests, json, urllib.parse, asyncio


nkey = os.environ['nkey']
rkey = os.environ['rkey']

def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
prefix = os.environ['prefix']

class Info(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def country(self, ctx,*,name=None):
    if not name:
      await ctx.send(embed=err(f"Country name is missing! Try again with {prefix}country <name>"))
    else:
      try:
        url = f'https://restcountries.eu/rest/v2/name/{name}?fullText=true'
        response = requests.request("GET", url=url)
        data = json.loads(response.text)
        name = str(data[0]["name"]) + " " + "("+ str(data[0]["nativeName"])+" - "+str(data[0]["alpha2Code"])+")"
        capital = data[0]["capital"]
        region = data[0]["region"]
        population = data[0]["population"]
        area = data[0]["area"]
        cur = str(data[0]["currencies"][0]["symbol"]) + " "+str(data[0]["currencies"][0]["name"]) + " ("+str(data[0]["currencies"][0]["code"])+")"
        c = data[0]["alpha2Code"]
        flag = f"https://www.countryflags.io/{c}/shiny/64.png"
        
        e = discord.Embed(title="", description=f"Capital: **{capital}**\nRegion: **{region}**\nPopulation: **{population}**\nArea: **{area}**\nCurrency: **{cur}**", color=ctx.author.color)
        e.set_author(name=name, icon_url=flag)

        await ctx.send(embed=e)
      except:
        await ctx.send(embed=err("Error! Try again with a valid response!"))
  
  @commands.command()
  async def weather(self, ctx,*,arg=None):
    if not arg:
      await ctx.send(embed=err(f"Place name is missing, please try again with {prefix}weather <place name>"))
    else:
      url = "https://community-open-weather-map.p.rapidapi.com/weather"

      querystring = {
          "q": arg,
          "units": "\"metric\" or \"imperial\""
      }

      headers = {
          'x-rapidapi-key': f"{rkey}",
          'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
      }

      response = requests.request("GET",
                                  url,
                                  headers=headers,
                                  params=querystring)

      json_data = json.loads(response.text)
      
      temp = round((json_data["main"]["temp"]) - 273.15, 2)
      overview = str(json_data["weather"][0]["main"]) + "/" + str(
          json_data["weather"][0]["description"])
      min = round((json_data["main"]["temp_min"]) - 273.15, 2)
      max = round((json_data["main"]["temp_max"]) - 273.15, 2)
      pressure = json_data["main"]["pressure"]
      humidty = json_data["main"]["humidity"]
      visibility = json_data["visibility"] / 1000
      windspeed = json_data["wind"]["speed"]
      name = json_data["name"]
      country = json_data["sys"]["country"]
      flag = f"https://www.countryflags.io/{country}/shiny/64.png"

      embed = discord.Embed(title="",
                            description=f"**Name:** {name}\n**Country**: {country}", color=discord.Color.blue())
      embed.add_field(
          name="Overview",
          value=
          f"**Overview:** {overview}\n**Temp:** {temp} °C\n**Min Temp:** {min} °C\n**Max Temp:** {max} °C",
          inline=True)
      embed.add_field(
          name="Extras",
          value=
          f"**Pressure:** {pressure} mbar\n**Visibility**: {visibility} km\n**Windspeed**: {windspeed} km/h\n**Humidity**: {humidty}%",
          inline=True)
      embed.set_author(name='Weather info!',icon_url=flag)
      await ctx.send(embed = embed)

  @commands.command()
  async def news(self, ctx,*,arg=None):
    if not arg:
      await ctx.send(embed=err(f"Please try again with a search term and page number! Type {prefix}help news for more info."))
    else:
      try:
        i = int(arg[-1])
      except ValueError:
        await ctx.send(embed=err(f"Please provide a page number for the result. 1 is the First page. Eg: {prefix}news <search term> 4, for the fourth page. Type {prefix}help news for more info."))
      else:
        if i == 0:
          pass
        else:
          i = i-1
        arg = arg[:-1]
        arg = urllib.parse.quote_plus(arg)
        
        url = f'https://newsapi.org/v2/everything?q={arg}&pageSize=5&apiKey={nkey}'
        response = requests.request("GET", url=url)
        data = json.loads(response.text)
        
        source = data["articles"][i]["source"]["name"]
        title= data["articles"][i]["title"]
        desc = data["articles"][i]["description"]
        url = data["articles"][i]["url"]
        img = data["articles"][i]["urlToImage"]

        embed = discord.Embed(title=title, description=desc, color=ctx.author.color, url=url)
        embed.set_author(name="Tény News", url=url, icon_url=img)
        embed.set_footer(text=f'Source: {source}')
        await ctx.send(embed=embed)
  
  @commands.command()
  async def covid(self, ctx, *, arg=None):
    if not arg:
      await ctx.send(embed=err("Try using this command with a country name!"))
    else:
      url = "https://covid-193.p.rapidapi.com/statistics"
      querystring = {"country":f"{arg}"}
      headers = {
          'x-rapidapi-key': f"{rkey}",
          'x-rapidapi-host': "covid-193.p.rapidapi.com"
          }

      response = requests.request("GET", url, headers=headers, params=querystring)
      data = json.loads(response.text)
      coun = str(data["parameters"]["country"]).title()
      tcase = data["response"][0]["cases"]["total"]
      acase = data["response"][0]["cases"]["active"]
      rec = data["response"][0]["cases"]["recovered"]
      death = data["response"][0]["deaths"]["total"]
      tcase = f"{tcase:,}"
      acase = f"{acase:,}"
      rec = f'{rec:,}'
      death = f'{death:,}'
      em = discord.Embed(title="Covid Stats!", description=f"Country: **{coun}**\n\nTotal Cases: **{tcase}**\nActive: **{acase}**\nRecovered: **{rec}**\n\nTotal Deaths: **{death}**", color=ctx.author.color)
      await ctx.send(embed=em)
  @commands.command()
  async def urban(self, ctx, *, arg=None):
    if not arg:
      await ctx.send(embed=err("Try giving an input term!"))
    else:
      url="https://mashape-community-urban-dictionary.p.rapidapi.com/define"
      querystring = {"term":f"{arg}"}

      headers = {
          'x-rapidapi-key': f"{rkey}",
          'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
          }

      response = requests.request("GET", url, headers=headers, params=querystring)
      data = json.loads(response.text)
      def terms(i):
        word = data["list"][i]["word"]
        define = data["list"][i]["definition"]
        link = data["list"][i]["permalink"]
        auth = data["list"][i]["author"]
        ex = data["list"][i]["example"]
        upv = data["list"][i]["thumbs_up"]
        downv = data["list"][i]["thumbs_down"]

        embed = discord.Embed(title=word, url=link, description=f"{define}\n\n**Example**: {ex}\nAuthor: {auth}", color=ctx.author.color)
        embed.set_footer(text=f"👍: {upv} | 👎: {downv}")
        return embed
      msg = await ctx.send(embed = terms(i=0))
      emotes= ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
      for e in emotes:
        await msg.add_reaction(e)
      def check(reaction, user):
        return( user == ctx.message.author and str(reaction.emoji) in emotes)
      o = 0
      while o == 0:
        try:
          reaction, user = await self.bot.wait_for('reaction_add', timeout=300,check=check)
          if(reaction.emoji=='1️⃣'):
            await msg.edit(embed=terms(0))
            await msg.remove_reaction('1️⃣',member=ctx.author)
          elif(reaction.emoji == '2️⃣'):
            await msg.edit(embed=terms(1))
            await msg.remove_reaction('2️⃣', member=ctx.author)
          elif(reaction.emoji == '3️⃣'):
            await msg.edit(embed=terms(2))
            await msg.remove_reaction('3️⃣', member=ctx.author)
          elif(reaction.emoji == '4️⃣'):
            await msg.edit(embed=terms(3))
            await msg.remove_reaction('4️⃣', member=ctx.author)
          elif(reaction.emoji == '5️⃣'):
            await msg.edit(embed=terms(4))
            await msg.remove_reaction('5️⃣', member=ctx.author)
        except asyncio.TimeoutError:
          o = 1

  
    
    
    
    

  
    
    

    
  











def setup(bot):
  bot.add_cog(Info(bot))