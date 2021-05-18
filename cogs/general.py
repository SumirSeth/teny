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
    try:
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
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()


  @commands.command()
  async def channels(self, ctx):
    try:
      bot = self.bot
      text_channel_list = []
      for channel in bot.get_all_channels():
          text_channel_list.append(channel)
      num_all = len(text_channel_list)

      if isinstance(ctx.channel, discord.channel.DMChannel):
        desc = f"**Use this command in a server to get server channel stats!**\n\n*The bot can see* **{num_all} channels** *including voice and text channels.*"
      else:
        ch = 0
        vc = 0
        ca = 0
        for channel in ctx.guild.text_channels:
          ch += 1
        for channel in ctx.guild.voice_channels:
          vc += 1
        for channel in ctx.guild.categories:
          ca += 1
        
        desc = f"**Text Channels:** ***{ch}***\n**Voice Channels:** ***{vc}***\n**Categories:** ***{ca}***\n**Total:** ***{ch+vc+ca}***\n\n*The bot can see* **{num_all} channels** *including voice and text channels.*"
      await ctx.send(embed = em(ctx, "Channel Info!", desc))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @commands.command()
  async def website(self, ctx):
    await ctx.send(embed = em(ctx, "My Website!", "http://teny.sumir.unaux.com"))
  
  

  @commands.command()
  async def whois(self, ctx, member:discord.Member=None):
    try:
      if not member:
        member = ctx.author

      name = member.name
      username = member
      nick = member.nick
      
      avatar = member.avatar_url
      created = member.created_at
      tim = created.strftime("%I:%M %p")
      year = created.strftime("%B %d, %Y")
      joined = member.joined_at
      tim_join = joined.strftime("%I:%M %p")
      year_join = joined.strftime("%B %d, %Y")

      roles = member.roles
      role_arg = ""
      for role in roles[1:]:
        role_arg = role_arg +" "+ role.mention


      perm_list = [perm[0] for perm in member.guild_permissions if perm[1]]
      perm = ""
      for i in perm_list:
        if "_" in i:
          i = i.title()
          perm = perm + ", " + i.replace("_", " ")
        else:
          perm = perm + ", " + i
      
      perm = perm[1:]


      emb = discord.Embed(title="", description=f"Mention: {member.mention}\nID:`{member.id}`\n{'Nickname: '+nick if nick!=None else ' '}", color = ctx.author.color)

      emb.set_author(name=username, url="http://teny.sumir.unaux.com", icon_url=avatar)
      emb.add_field(name="Joined", value=f"**{year_join}** at **{tim_join}**")
    
      emb.add_field(name="Created", value=f"**{year}** at **{tim}**")
      emb.add_field(name="Roles", value=role_arg, inline=False)
      emb.add_field(name="Permissions", value=perm)
      emb.set_thumbnail(url = avatar)
      emb.set_footer(text=f"In {member.guild.name}", icon_url=member.guild.icon_url)
      await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @commands.command(aliases=["av"])
  async def avatar(self, ctx, member:discord.Member=None):
    try:
      if not member:
        member = ctx.author
      avatar_png = member.avatar_url_as(format="png")
      avatar_jpg = member.avatar_url_as(format="jpg")
      avatar_fk = member.avatar_url_as(format="png", size=4096)
      avatar = member.avatar_url
      await ctx.send(embed = em(ctx, f"Avatar - {member.name}", f"Links:\n[**PNG**]({avatar_png}) | [**JPG**]({avatar_jpg}) | [**4K**]({avatar_fk})").set_image(url = avatar))
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  
    
  @commands.command()
  async def com(self, ctx):
    for c in self.bot.walk_commands():
      print(c)

  @commands.command()
  async def messages(self, ctx, u1:discord.Member=None):
    print(0)
    


    




























def setup(bot):
  bot.add_cog(General(bot))