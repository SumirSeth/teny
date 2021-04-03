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
    e.add_field(name="Info", value=f"`{prefix}country <name>`, `{prefix}weather <place>`, `{prefix}news <search term> <page number>`, `{prefix}covid <country name>`, `{prefix}urban <search term>`", inline=False)
    e.add_field(name="Fun", value=f"`{prefix}hug <user>`, `{prefix}lovecal <name 1> <name 2>`, `{prefix}advice`, `{prefix}bill`, `{prefix}kanye`, `{prefix}gay`, `{prefix}pp`", inline=False)
    e.add_field(name="Joke", value=f"`{prefix}joke <category name>`. Categories: `programming (pro)`, `miscellaneous (misc)`, `dark (d)`, `pun (p)`, `spooky (sp)`, `christmas (chr)`, `dadjoke(dad)`\n\nType `{prefix}joke` for more info!")
    e.add_field(name="Bot", value=f"`{prefix}contact <Your issue to the dev>`, `{prefix}invite`", inline=False)
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
  @help.command(aliases=['chr', 'p', 'ch', 'pro', 'misc', 'd', 'sp', 'programming', 'miscellaneous', 'dark', 'pun', 'spooky', 'christmas', 'dad', 'dadjoke'])
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


def setup(bot):
  bot.add_cog(Help(bot))