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
    await self.bot.change_presence(activity=discord.Game(name="type t,help | Dev: Spookie :D"))


  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    e = discord.Embed(title="Help", description=f"Type {prefix}help <command> for more info.", color=ctx.author.color)

    e.add_field(name="Fact", value=f"`{prefix}fact <category name>`. Categories: `cat`, `anime`, `useless`, `chuck`, `num`, `dog`\n\nType `{prefix}fact` for more info!", inline=True)

    e.add_field(name="Info", value=f"`{prefix}country <name>`, `{prefix}weather <place>`, `{prefix}news <search term> <page number>`, `{prefix}covid <country name>`, `{prefix}urban <search term>`, `{prefix}wiki <search term>`, `{prefix}curcon`", inline=False)

    e.add_field(name="Fun", value=f"`{prefix}hug <user (optional)>`,`{prefix}wink <user (optional)>`, `{prefix}lovecal <name 1> <name 2>`, `{prefix}advice`,`{prefix}quote`, `{prefix}bill`, `{prefix}kanye`, `{prefix}gay`, `{prefix}pp`, `{prefix}meme`, `{prefix}8ball <question>`, `{prefix}monke`, `{prefix}doge <text>`, `{prefix}aff`, `{prefix}y/n <question>`", inline=False)

    e.add_field(name="Joke", value=f"`{prefix}joke <category name>`. Categories: `programming (pro)`, `miscellaneous (misc)`, `dark (d)`, `pun (p)`, `spooky (sp)`, `christmas (chr)`, `dadjoke(dad)`, `yomom`, `bread`\n\nType `{prefix}joke` for more info!")

    e.add_field(name="Random", value=f"`{prefix}random <category>`. Categories: `cat`, `dog`, `fox`, `panda`, `redpanda`, `bird`, `koala`, `image`, `color`",inline=False)

    e.add_field(name="Bot", value=f"`{prefix}contact <Your issue to the dev>`, `{prefix}invite`", inline=False)
    
    e.set_footer(text="By Spookie_Stunkk/Sumir")
    await ctx.send(embed=e)
    


  @help.command(aliases=['cat', 'dog', 'anime', 'useless', 'chuck', 'num'])
  async def fact(self, ctx):
    await ctx.send(f"Type `{prefix}fact` for more info.")

  @help.command()
  async def country(self, ctx):
    e = discord.Embed(title="Country!", description=f"Get any countries info!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}country <name>`")
    await ctx.send(embed=e)
  @help.command()
  async def weather(self, ctx):
    e = discord.Embed(title="Weather!", description=f"Get any place's weather info!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}weather <place>`")
    await ctx.send(embed=e)
  @help.command()
  async def hug(self, ctx):
    e = discord.Embed(title="Hug!", description=f"Hug anyone!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}hug <user>`")
    await ctx.send(embed=e)
  @help.command()
  async def lovecal(self, ctx):
    e = discord.Embed(title="Love Calculator!", description=f"Calculate love % between 2 people!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}lovecal <name 1> <name 2>`")
    await ctx.send(embed=e)
  @help.command()
  async def news(self, ctx):
    e = discord.Embed(title="News!", description=f"Get the breaking news for any search term!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}news <search term> <page number>`")
    e.add_field(name="Example", value=f"`{prefix}news Elon Musk 1`\nWhere 'Elon Musk' is the search term and '1' is the result page number!")
    await ctx.send(embed=e)
  @help.command()
  async def covid(self, ctx):
    e = discord.Embed(title="Covid!", description=f"Get the covid stats for any country!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}covid <country name>`")
    await ctx.send(embed=e)
  @help.command()
  async def urban(self, ctx):
    e = discord.Embed(title="Urban Dictionary!", description=f"Get definition of any word from urban dictionary!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}urban <search term>`")
    await ctx.send(embed=e)
  @help.command(aliases=['chr', 'p', 'ch', 'pro', 'misc', 'd', 'sp', 'programming', 'miscellaneous', 'dark', 'pun', 'spooky', 'christmas', 'dad', 'dadjoke', 'yomom', 'bread'])
  async def joke(self, ctx):
    await ctx.send(f"Type `{prefix}joke` to get more info.")
  @help.command()
  async def advice(self, ctx):
    e = discord.Embed(title="Advice For You!", description=f"Get an advice from the bot!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}advice`")
    await ctx.send(embed=e)
  @help.command()
  async def bill(self, ctx):
    e = discord.Embed(title="Be like bill!", description=f"Be like bill images!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}bill`")
    await ctx.send(embed=e)
  @help.command()
  async def kanye(self, ctx):
    e = discord.Embed(title="Kanye West Quotes!", description=f"Get random Kanye West Quotes!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}kanye`")
    await ctx.send(embed=e)
  @help.command()
  async def gay(self, ctx):
    e = discord.Embed(title="Gay Rates!", description=f"See how gay you or your friends' are!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}gay` | `{prefix}gay @mention/id/username`")
    await ctx.send(embed=e)
  @help.command()
  async def pp(self, ctx):
    e = discord.Embed(title="PP Size!", description=f"See how big is your or your friends' pp!", color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}pp` | `{prefix}pp @mention/id/username`")
    await ctx.send(embed=e)
  @help.command()
  async def wiki(self, ctx):
    e = discord.Embed(title="Wikipedia Info!", description=f"Get info from Wikipedia for any thing! (beta command)" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}wiki <search term>`")
    await ctx.send(embed=e)
  @help.command()
  async def quote(self, ctx):
    e = discord.Embed(title="Random Quote!", description=f"Get a random quotes!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}quote`")
    await ctx.send(embed=e)
  @help.command()
  async def meme(self, ctx):
    e = discord.Embed(title="Random Meme!", description=f"Get a random meme!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}meme`")
    await ctx.send(embed=e)
  @help.command(aliases=["8Ball","8ball"])
  async def eightball(self, ctx):
    e = discord.Embed(title="8 Ball!", description=f"Get the bot to answer any of your question!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}8ball <question>`")
    
    e.add_field(name="**Aliases**", value=f"Aliases: `{prefix}8ball`, `{prefix}eightball`, `{prefix}8Ball`", inline=False)
    await ctx.send(embed=e)
  @help.command()
  async def monke(self,ctx):
    e = discord.Embed(title="Monke!", description=f"Get a random monkey photo!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}monke`")
    await ctx.send(embed=e)
  @help.command()
  async def curcon(self, ctx):
    e = discord.Embed(title="Currency Converter and Info!", description=f"Get currency conversions and info with one command!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"Syntax is divided into 2 parts, you can either request two specific currencies or request USD values of all available currencies. More info below!\n\n**For all currencies value of USD type:** `{prefix}curcon all`\n\n**For conversion rate between 2 specific currencies type: **`{prefix}curcon <first currency> <second currency>`")
    e.add_field(name="Examples", value=f"For conversion rate between 2 specific currencies, USD and INR for this example: `{prefix}curcon usd inr`")
    await ctx.send(embed=e)

  @help.command(aliases=["random cat", "random dog", "random fox", "random image"])
  async def random(self, ctx):
    e = discord.Embed(title="Randomness", description=f"Get random things from different categories!", color=ctx.author.color)
    e.add_field(name="Categories", value="cat, dog, fox, panda, redpanda, bird, koala, image, color", inline=False)
    e.add_field(name="Syntax", value=f"`{prefix}random <category>`", inline=False)
    e.add_field(name="Examples", value=f"For random cat picture do: `{prefix}random cat`\nFor random images from unsplash do: `{prefix}random image`")
    await ctx.send(embed=e)
  
  @help.command()
  async def doge(self, ctx):
    e = discord.Embed(title="Doge Translations!", description=f"Get your words in the form of doge language!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}doge <text>`")
    await ctx.send(embed=e)

  @help.command()
  async def aff(self, ctx):
    e = discord.Embed(title="Affirmations!", description=f"Get words of affirmation from the bot!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}aff`")
    await ctx.send(embed=e)

  @help.command(aliases=["y/n"])
  async def yesno(self, ctx):
    e = discord.Embed(title="Yes or No?", description=f"Get answer of a question with a yes or no with a gif from the bot!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}y/n <arg>`")
    e.add_field(name="Aliases", value=f"`{prefix}yesno <arg>`")
    await ctx.send(embed=e)


















def setup(bot):
  bot.add_cog(Help(bot))