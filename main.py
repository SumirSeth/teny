from keep_alive import keep_alive
import os
import discord
from discord.ext import commands,tasks
import requests, json, io, contextlib


#------------------CONFIGS------------------
token = os.environ['TOKEN']
prefix = os.environ['prefix']

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=["t,", "T,", "<@!824888045622394910> ", "<@824888045622394910> ", "teny ", "Teny ", "Tény ", "tény "], help_command=None,intents=intents)

owner = [740845704326676493, 575263293015588867]
#------------------CONFIGS------------------
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er


#------------------COMMANDS------------------

@bot.event
async def on_ready():
  print("100% loaded!")

@bot.command()
async def ping(ctx):
    if round(bot.latency * 1000) <= 50:
        embed = discord.Embed(
            title="PING",
            description=
            f":ping_pong: Pong! The ping is **{round(bot.latency *1000)}** milliseconds!",
            color=0x44ff44)
    elif round(bot.latency * 1000) <= 100:
        embed = discord.Embed(
            title="PING",
            description=
            f":ping_pong: Pong! The ping is **{round(bot.latency *1000)}** milliseconds!",
            color=0xffd000)
    elif round(bot.latency * 1000) <= 200:
        embed = discord.Embed(
            title="PING",
            description=
            f":ping_pong: Pong! The ping is **{round(bot.latency *1000)}** milliseconds!",
            color=0xff6600)
    else:
        embed = discord.Embed(
            title="PING",
            description=
            f":ping_pong: Pong! The ping is **{round(bot.latency *1000)}** milliseconds!",
            color=0x990000)
    embed.set_image(url = f"https://falsiskremlin.sirv.com/resim_2020-11-28_113400.png?text.0.text={round(bot.latency*1000)}%20ms&text.0.position.x=-10%25&text.0.position.y=-25%25&text.0.size=60&text.0.color=ffffff&text.0.font.family=Play&watermark.0.image=%2FImages%2Fresim_2020-11-28_113954.png&watermark.0.position.x=-35%25&watermark.0.scale.width=200&watermark.0.scale.height=200")
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def contact(ctx, *, arg):
  #https://discord.com/api/oauth2/authorize?client_id=824888045622394910&permissions=2352340160&scope=bot
  channel = bot.get_channel(825733074674909224)
  em = discord.Embed(title=f"New report from {ctx.author.name}", description=arg, color = discord.Color.blurple())
  em.set_footer(text=f"From {ctx.guild.name}")
  msg = await channel.send(embed=em)
  for i in ['⬆️', '⬇️']:
    await msg.add_reaction(i)
  await ctx.send("Reported!")
@contact.error
async def contact_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send(embed=err("This command is on cooldown. Cooldown time: 1 hour."))
  else:
    raise error
@bot.command()
async def invite(ctx):
  e = discord.Embed(title="Invite Me!", url="https://discord.com/api/oauth2/authorize?client_id=824888045622394910&permissions=3723869398&scope=bot", color=ctx.author.color)
  await ctx.send(embed=e)
@bot.command()
async def vote(ctx):
  e = discord.Embed(title="Vote for me!", description="[**Vote!**](https://top.gg/bot/824888045622394910/vote)\n\n[**Check bot's Top.gg page**](https://top.gg/bot/824888045622394910)\n\n[**Check bot's DBL page**](https://botdesignerlist.com/bot/KkNNjmaN9ZrDFkYAvovX)\n[Vote on DBL](https://botdesignerlist.com/bot/KkNNjmaN9ZrDFkYAvovX#rate-bot)",color=ctx.author.color)
  await ctx.send(embed = e)

@bot.command()
async def servers(ctx):
  if ctx.author.id == owner[1] or owner[0]:
    a = ''
    o = 0
    async for i in bot.fetch_guilds():
      a = a + ", "+ '`'+str(i)+'`'
      o = o + 1
    await ctx.send(f'{a}\n{o}')

@commands.bot_has_permissions(send_messages=True)
@bot.event 
async def on_message(message):
  if message.content == "<@!824888045622394910>" or message.content == "<@824888045622394910>":
    embed = discord.Embed(title="Tény!", description=f"Hello! My prefix is `{prefix}`!\nType `{prefix}help` for more info.\n\n**Invite Me:** [INVITE](https://discord.com/api/oauth2/authorize?client_id=824888045622394910&permissions=3723869398&scope=bot)\n**Contact server:** [Server](https://discord.gg/cVvXNgj5D2)\n**Dev:** Spookie_Stunkk/Sumir", color=message.author.color)
    await message.channel.send(embed=embed)
  await bot.process_commands(message)




@bot.command()
async def eval(ctx, *, code):
  if(ctx.author.id ==owner[0]or owner[1]):
      str_obj = io.StringIO()
      try:
          with contextlib.redirect_stdout(str_obj):
              exec(code)
      except Exception as e:
          return await ctx.send(f"```{e.__class__.__name__}: {e}```")
      await ctx.send(f'```{str_obj.getvalue()}```')



#------------------COMMANDS------------------

#---cogs commands---
@bot.command()
async def load(ctx, extension):
  if ctx.author.id == owner[0] or ctx.author.id == owner[1]:
    try:
      bot.load_extension(f'cogs.{extension}')
      await ctx.send(f"Loaded {extension} cog!")
    except:
      await ctx.send("Cog might already be loaded!")
  else:
    pass
@bot.command()
async def unload(ctx, extension):
  if ctx.author.id == owner[0] or ctx.author.id == owner[1]:
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Unoaded {extension} cog!")
  else:
    pass

@bot.command()
async def reload(ctx, extension):
  if ctx.author.id == owner[0] or ctx.author.id == owner[1]:
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send("Reloaded {}".format(extension))
  else:
    pass
#---cogs commands---




#------------------RUN------------------
keep_alive()
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)  