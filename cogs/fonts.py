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



class Fonts(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True)
  async def fonts(self, ctx):
    await ctx.send(embed = em(ctx, "Sub Category for Text Fonts", f"Uses-> `{prefix}fonts <category>`").add_field(name="Categories", value="Available Fonts: oxygene, gold, strongman, neon, fluffy, tweeter, fancy, metal, dance, disco, booking, scrible, flame, craft").add_field(name="Syntax", value=f"{prefix}fonts <category> <text>\n\nEg: {prefix}fonts gold <text>", inline=False))



  @fonts.command()
  async def oxygene(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://gdcolon.com/tools/gdlogo/img/{arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @fonts.command()
  async def gold(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://habbofont.net/font/steampunk/{arg}.gif"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @fonts.command()
  async def strongman(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=strongman-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
    
  @fonts.command()
  async def neon(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=neon-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
    
  @fonts.command()
  async def fluffy(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=fluffy-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @fonts.command()
  async def tweeter(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=birdy-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @fonts.command()
  async def fancy(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=fancy-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @fonts.command()
  async def metal(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=brushed-metal-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @fonts.command()
  async def dance(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=dance-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @fonts.command()
  async def disco(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=disco-party-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()


  @fonts.command()
  async def booking(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=booking-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
    
  @fonts.command()
  async def scribble(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?script=scribble-logo&text={arg}&_loc=generate&fontname=GoodCityModern&shadowType=0&autocrop=on&autocropPadding=100&imageoutput=true"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
    
  @fonts.command()
  async def flame(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=flame-logo&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
  
  @fonts.command()
  async def craft(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://flamingtext.com/net-fu/proxy_form.cgi?script=crafts-logo&text={arg}&_loc=generate&imageoutput=true"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()
    
  @commands.group(invoke_without_command=True)
  async def logos(self, ctx):
    await ctx.send(embed = em(ctx, "Sub Category for Logos", f"Uses-> `{prefix}logo <category>`").add_field(name="Categories", value="Available Fonts: green, simple, bold").add_field(name="Syntax", value=f"{prefix}logo <category> <text>\n\nEg: {prefix}logo green <text>", inline=False))
  
  @logos.command()
  async def green(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://dynamic.brandcrowd.com/asset/logo/7f0254b2-49ae-4819-9107-47728665a65f/logo?v=4&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @logos.command()
  async def simple(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://dynamic.brandcrowd.com/asset/logo/1a2ebc7a-1b24-466a-bee7-9a0e8f5d8395/logo?v=4&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()

  @logos.command()
  async def bold(self, ctx, *, arg=None):
    try:
      if not arg:
        await ctx.send(embed = err("Please provide an argument!"))
      else:
        arg = arg.replace(" ", "%20")
        url = f"https://dynamic.brandcrowd.com/asset/logo/f802ad87-f5ae-491f-9a02-89ee701b588f/logo?v=4&text={arg}"
        emb = em(ctx, "", "")
        emb.set_image(url = url)
        await ctx.send(embed = emb)
    except Exception as e:
      await ctx.send("Error! Try later.")
      with open("/home/runner/teny/error-log.txt", "a") as f:
        f.write(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}\n")
        f.close()





































def setup(bot):
  bot.add_cog(Fonts(bot))