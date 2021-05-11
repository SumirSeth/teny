import discord
from discord.ext import commands
import os, asyncio, requests, json

def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
prefix = os.environ['prefix']


class Trivia(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.group(invoke_without_command=True)
  async def trivia(self, ctx):
    embed = em(ctx, "Trivia", "A sub category for Trivia related commands!")
    embed.add_field(name="Commands", value=f"`{prefix}random`")
    await ctx.send(embed=embed)

  
  @trivia.command()
  async def random(self, ctx):
    url = "http://jservice.io/api/random"
    data = json.loads(requests.request("GET", url=url).text)
    q = data[0]["question"]
    a = data[0]["answer"]
    h = data[0]["value"]
    c = data[0]["category"]["title"]
    msg = await ctx.send(embed = em(ctx, "","The bot will show the answer in 5s!"))
    await asyncio.sleep(2)
    await msg.edit(embed = em(ctx, "Random Trivia", f"{'Hardness: **'+str(int(h)/100)+'**' if h!=None else ''}\nCategory: **{c.title()}**").add_field(name="Question:", value=q))
    await asyncio.sleep(6)
    await msg.edit(embed = em(ctx, "Random Trivia", f"Hardness: **{int(h)/100}/10**\nCategory: **{c.title()}**").add_field(name="Question:", value=q).add_field(name="Answer:",value=a, inline=False))




  



  @trivia.command()
  async def start(self, ctx, opt, u1:discord.Member=None, u2:discord.Member=None, u3:discord.Member=None, u4:discord.Member=None, u5:discord.Member=None):
    global track, chances
    chances = {}
    track = {}
    if not opt:
      emb = em(ctx, "Trivia Start Options", "You can opt between choosing `MCQ` type questions or `True/False` type questions.").add_field(name="Syntax", value=f"For MCQ type questions: `{prefix}trivia start mcq`\nFor True/False type questions: `{prefix}trivia start tf`")
      await ctx.send(embed = emb)
    else:
    #trivia start mcq
      if opt.lower() == "mcq":
        if not u1 or not u2:
          await ctx.send(embed = err(f"Atleast 2 players are needed! For only single trivias, type `{prefix}trivia random`"))
        else:
          mem = [u1, u2, u3, u4, u5]
          for m in mem:
            if not m:
              pass
            else:
              track.update({f"{m}": 0})
              chances.update({f"{m}":1})
          msg = await ctx.send(embed = em(ctx, f"Trivia MCQ Type- {len(track)} members", f"First to get {'3 points' if not u4 and not u5 else '2 points'} wins!\nThe bot will edit this message with questions until one of the player gets {'3 points' if not u4 and not u5 else '2 points'} or the time is out, for which the bot will inform and declare winner/loser/draw according to the points.\n\nThis message will stay visible for 10s."))

          emotes = ['1️⃣', '2️⃣', '3️⃣']
          for emote in emotes:
            await msg.add_reaction(emote)
          await asyncio.sleep(10)
          await msg.edit(embed = em(ctx, f"Trivia MCQ Type- {len(track)} members", "You will be able to react to give answers, the bot will accept reaction from only the person whose turn it is.\n\nStarting in 2s."))
          await asyncio.sleep(3)

          url = "https://opentdb.com/api.php?amount=1&type=multiple"
          def feed():
            data = json.loads(requests.request("GET", url=url).text)
            return data
          
          def check(reaction, user):
            return( user == u1 or user==u2 or user==u3 or user==u4 or user==u5 and str(reaction.emoji) in emotes)
          
          c = 0
          while c==0:
            try:
              reaction, user = await self.bot.wait_for('reaction_add', timeout=600,check=check)
              chances[f"{u1}"] = 0

              




            except asyncio.TimeoutError:
              c = 1
          
    

























































def setup(bot):
  bot.add_cog(Trivia(bot))