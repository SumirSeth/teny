import discord
from discord.ext import commands
import os


def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
prefix = os.environ['prefix']


class General(commands.Cog):

  def __init__(self, bot):
    self.bot = bot



  @commands.command()
  async def poll(self, ctx, *, arg):
    try:
      arg = arg.split("|")
      title = arg[0]
      emo = {
        1:"1️⃣",
        2:"2️⃣",
        3:"3️⃣",
        4:"4️⃣",
        5:"5️⃣",
        6:"6️⃣",
        7:"7️⃣",
        8:"8️⃣",
        9:"9️⃣",
        10:"🔟"
      }
      a = ""
      for i in range(1,len(arg)):
        a = a + f'{emo[i]} {arg[i]}' + '\n'
      message = await ctx.send(embed = em(ctx, title,a))
      for i in range(1, len(arg)):
        await message.add_reaction(f'{emo[i]}')
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @commands.command()
  async def members(self, ctx):
    
    guilds = self.bot.guilds
    members = 0
    for guild in guilds:
      members += len(guild.members)
    
    
    members_set = set()
    for guild in guilds:
      for member in guild.members:
          members_set.add(member)
    uniq_members = len(members_set)
    

    
    if isinstance(ctx.channel, discord.channel.DMChannel):
          desc = f"**Use this command in a server, to get server members too!**\n\n*The bot is serving* **{members} members** *in total*, and **{uniq_members} unique members!** "
    else:
      a=ctx.guild.member_count
      desc = f"**Members in** ***{ctx.guild.name:}*** **:** {a}\n\n*The bot is serving* **{members} members** *in total*, and **{uniq_members} unique members!** "
    await ctx.send(embed=em(ctx, f"Members Info!", desc))




























def setup(bot):
  bot.add_cog(General(bot))