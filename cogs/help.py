import discord
from discord.ext import commands
import os, asyncio

prefix = os.environ['prefix']
class Help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("Cog ready!")
    await self.bot.change_presence(activity=discord.Game(name="type t,help | Dev: Spookie :D"))


  @commands.group(invoke_without_command=True)
  async def help(self, ctx, arg:int=None):


    def h(a):
      emb = discord.Embed(title="", description=f"Type {prefix}help <command> for more info.", color=ctx.author.color) 
      emb.set_author(name = "Help", url="", icon_url="https://cdn.discordapp.com/attachments/825992733960175616/836626787546562641/1f6e0.png")
      
      if a == 0:
        emb.add_field(name="<:info:836638112394117160> Fact", value=f"<a:st:836663594262200390> `{prefix}fact <category name>`. Categories: `cat`, `anime`, `useless`, `chuck`, `num`, `dog`\n\nType `{prefix}fact` for more info!", inline=True)
        emb.add_field(name="<:info:836638112394117160> Info", value=f"<a:st:836663594262200390> `{prefix}country <name>`, `{prefix}weather <place>`, `{prefix}news <search term> <page number>`, `{prefix}covid <country name>`, `{prefix}urban <search term>`, `{prefix}wiki <search term>`, `{prefix}curcon`, `{prefix}lyrics <song name>`", inline=False)
      elif a==1:
        emb.add_field(name="<:info:836638112394117160> General", value=f"<a:st:836663594262200390> `{prefix}ping`, `{prefix}help`, `{prefix}poll <title|option1|option2|...option10>`, `{prefix}members`, `{prefix}channels`, `{prefix}oxygene <text>`, `{prefix}gold <text>`, `{prefix}whois <member (optional)>`, `{prefix}av <member>(optional)`, `{prefix}website`", inline=True)
        emb.add_field(name="<:info:836638112394117160> Fun", value=f"<a:st:836663594262200390> `{prefix}hug <user (optional)>`,`{prefix}wink <user (optional)>`, `{prefix}lovecal <name 1> <name 2>`, `{prefix}advice`,`{prefix}quote`, `{prefix}bill`, `{prefix}kanye`, `{prefix}gay`, `{prefix}pp`, `{prefix}meme`, `{prefix}8ball <question>`, `{prefix}monke`, `{prefix}doge <text>`, `{prefix}aff`, `{prefix}y/n <question>`", inline=False)
      elif a == 2:
        emb.add_field(name="<:info:836638112394117160> Joke", value=f"<a:st:836663594262200390> `{prefix}joke <category name>`. Categories: `programming (pro)`, `miscellaneous (misc)`, `dark (d)`, `pun (p)`, `spooky (sp)`, `christmas (chr)`, `dadjoke(dad)`, `yomom`, `bread`\n\nType `{prefix}joke` for more info!")
        emb.add_field(name="<:info:836638112394117160> Meme-Gen, Text & Image Manipulation", value=f"<a:st:836663594262200390> `{prefix}eject <user> <imposter> <crewmate color>(type {prefix}help eject for more info!)`, `{prefix}drip <user(@mention/user id/username/name/nickname)>`, `{prefix}stonks <user(@mention/user id/username/name/nickname)>`, `{prefix}batman <user1> <user2> <arg>`, `{prefix}carreverse <text>`, `{prefix}changemymind <text>`, `{prefix}firsttime <user>`, `{prefix}grave <user>`, `{prefix}trash <user>`, `{prefix}magik <user>`, `{prefix}emojify <text>`, `{prefix}reverse <text>`, `{prefix}spank <user1> <user2>(optional)`", inline=False)
      elif a==3:
        emb.add_field(name="<:info:836638112394117160> Random", value=f"<a:st:836663594262200390> `{prefix}random <category>`. Categories: `cat`, `dog`, `fox`, `panda`, `redpanda`, `bird`, `koala`, `image`, `color`, `waifu`",inline=False)
        emb.add_field(name="<:info:836638112394117160> Fonts and Logos", value=f"<a:st:836663594262200390> `{prefix}fonts <category>`. Categories: `oxygene`, `gold`, `strongman`, `neon`, `fluffy`, `tweeter`, `fancy`, `metal`, `dance`, `party`, `booking`, `scribble`, `flame`, `craft`\n\n<a:st:836663594262200390> `{prefix}logos <category>`. Categories: `green`, `bold`, `simple`",inline=False)
        
      elif a == 4:
        emb.add_field(name="<:info:836638112394117160> Bot", value=f"<a:st:836663594262200390> `{prefix}contact <Your issue to the dev>`, `{prefix}invite`, `{prefix}vote`\n\n**Checkout Bots Website: [Click here](http://teny.sumir.unaux.com)**", inline=True)
        emb.add_field(name="🔴Invite Bot", value="<a:st:836663594262200390> [**Click here!**](https://discord.com/api/oauth2/authorize?client_id=824888045622394910&permissions=3723869398&scope=bot)", inline=False)
      emb.set_footer(text=f"Page: {a+1}/5 | By Spookie_Stunkk/Sumir")

      return emb

    if not arg:
      msg = await ctx.send(embed=h(0))


      emotes= ["⏪","◀️", "▶️","⏩"]
      for e in emotes:
        await msg.add_reaction(e)
      def check(reaction, user):
        return( user == ctx.message.author and str(reaction.emoji) in emotes)
      
      o = 0
      rnum = 0
      m = 0
      while o==0:
        try:
          reaction, user = await self.bot.wait_for('reaction_add', timeout=120,check=check)
          
          if reaction.emoji == "◀️":
            if rnum == 0:
              pass
            else:
              rnum -= 1
            await msg.edit(embed = h(rnum))
            try:
              await msg.remove_reaction('◀️',member=ctx.author)
            except:
              if m == 0:
                await ctx.send("Please give me reaction add and remove perms to function with the reaction controls properly.")
                m = 1
              else:
                pass

          if reaction.emoji == "▶️":
            if rnum == 4:
              pass
            else:
              rnum += 1
            await msg.edit(embed = h(rnum))
            try:
              await msg.remove_reaction('▶️',member=ctx.author)
            except:
              if m == 0:
                await ctx.send("Please give me reaction add and remove perms to function with the reaction controls properly.")
                m = 1
              else:
                pass
          
          if reaction.emoji == "⏪":
            await msg.edit(embed = h(0))
            rnum = 0
            try:
              await msg.remove_reaction("⏪", member=ctx.author)
            except:
              if m == 0:
                await ctx.send("Please give me reaction add and remove perms to function with the reaction controls properly.")
                m = 1
              else:
                pass
          

          if reaction.emoji == "⏩":
            await msg.edit(embed = h(4))
            rnum = 4
            try:
              await msg.remove_reaction("⏩", member=ctx.author)
            except:
              if m == 0:
                await ctx.send("Please give me reaction add and remove perms to function with the reaction controls properly.")
                m = 1
              else:
                pass

        except asyncio.TimeoutError:
          o = 1
    elif int(arg)==1 or arg==2 or arg==3 or arg==4 or arg==5:
      await ctx.send(embed = h(arg-1))
    


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
  
  @help.command()
  async def poll(self, ctx):
    e = discord.Embed(title="Polls!", description=f"Make a poll with maximum 10 options!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}poll <title|option1|option2|...option10>`")
    await ctx.send(embed=e)

  @help.command()
  async def members(self, ctx):
    e = discord.Embed(title="Member Info!", description=f"Get member info of the server and the bot together!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}members`")
    await ctx.send(embed=e)
  @help.command()
  async def channels(self, ctx):
    e = discord.Embed(title="Channels Info!", description=f"Get channel info of the server and the bot together!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}channels`")
    await ctx.send(embed=e)
  
  
  @help.command()
  async def whois(self, ctx):
    e = discord.Embed(title="Member Info!", description=f"Get a members every useful info with one command!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}whois <member>(optional)`\n\nIf member is not provided, it returns the info of user of who initiated the command!")
    await ctx.send(embed=e)

  @help.command(aliases=["avatar"])
  async def av(self, ctx):
    e = discord.Embed(title="Avatar!", description=f"Get a members avatar with links to PNG, JPG and even 4K images.!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}avatar <member>(optional)`\n\nIf member is not provided, it returns avatar of user of who initiated the command!")
    await ctx.send(embed=e)
  @help.command()
  async def eject(self, ctx):
    e = discord.Embed(title="Amogus!", description=f"Get an Among Us imposter edited picture!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}eject <user> <imposter> <crewmate color>`")
    e.add_field(name="**Example**", value=f"You can leave imposter and crew mate color empty for it to be random! Imposter decides whether the user gets imposter or not! You can type true or false for it to work. Eg: `{prefix}eject <user> false`\nImposter color you can choose from are: ['black','blue','brown','cyan','darkgreen','lime','orange','pink','purple','red','white','yellow'], Eg: `{prefix}eject <user> true cyan`")
    await ctx.send(embed=e)
  @help.command()
  async def lyrics(self, ctx):
    e = discord.Embed(title="Lyrics!", description=f"Get lyrics of a song!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}lyrics <song name>`")
    await ctx.send(embed=e)
  @help.command()
  async def drip(self, ctx):
    e = discord.Embed(title="Drip!", description=f"Get drip edited picture with pfp!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}drip <user>`")
    await ctx.send(embed=e)
  @help.command()
  async def stonks(self, ctx):
    e = discord.Embed(title="Stonks!", description=f"Get stonks edited picture with pfp!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}stonks <user>`")
    await ctx.send(embed=e)
  
  @help.command()
  async def batman(self, ctx):
    e = discord.Embed(title="Bat Man!", description=f"Get batman edited picture with pfp!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}batman <user1> <user2> <text|text2>`")
    e.add_field(name="**Example**", value=f"User is a discord member which the bot can access using their @mention/uerid/username/nickname etc.\n\nThe command reqired 2 users and 2 texts joined by a '|'.\n\nAssume we have user x and user y, we can write: `{prefix}batman @x @y <text|text2>`.\nThe first user mentioned will be considered batman and the 'text1' will be said by x in the image hence y will say 'text'.", inline=False)
    
    await ctx.send(embed=e)
  
  @help.command()
  async def carreverse(self, ctx):
    e = discord.Embed(title="Car Revese Meme!", description=f"Get car reverse edited picture with custom text!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}carreverse <text>`")
    await ctx.send(embed=e)

  @help.command()
  async def changemymind(self, ctx):
    e = discord.Embed(title="Chany My Mind!", description=f"Get change my mind edited picture with custom text!" , color=ctx.author.color)
    e.add_field(name="**Syntax**", value=f"`{prefix}changemymind <text>`")
    await ctx.send(embed=e)

  @help.command(aliases=["oxygene", "gold", "strongman", "neon", "fluffy", "tweeter", "fancy", "metal", "dance", "party", "booking"])
  async def fonts(self, ctx):
    await ctx.send(f"Depreciated. Please use `{prefix}fonts` to for info.")














def setup(bot):
  bot.add_cog(Help(bot))