import discord
from discord.ext import commands
import os
import requests, json

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
  async def news(self, ctx):
    url = f'https://newsapi.org/v2/everything?q=Apple&from=2021-03-27&sortBy=popularity&apiKey={nkey}'
    response = requests.request("GET", url=url)
    data = json.loads(response.text)
    await ctx.send(data["totalResults"])
    











def setup(bot):
  bot.add_cog(Info(bot))