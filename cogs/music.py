import discord
from discord.ext import commands,tasks
import os
import youtube_dl

prefix = os.environ['prefix']
def em(ctx,title, msg):
  e = discord.Embed(title=title, description=msg, color= ctx.author.color)
  return e
def err(msg):
  er = discord.Embed(title="", description='', color=0xe74c3c)
  er.set_author(name=msg,icon_url="https://cdn.discordapp.com/attachments/804212727869866006/824902921505865749/772509.png")
  return er
'''-----------------------'''
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename



class Music(commands.Cog):

  def __init__(self, bot):
    self.bot = bot




  @commands.command()
  async def join(self, ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send(f"Joined {ctx.message.author.voice.channel.name}")

  @commands.command(name='leave', help='To make the bot leave the voice channel')
  async def leave(self, ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send(f"Left the channel!")
    else:
        await ctx.send("The bot is not connected to a voice channel.")
    
  @commands.command()
  async def play(self, ctx, url=None):
    if not url:
      await ctx.send(embed=err("Enter a URL!"))
    else:
      try:
          server = ctx.message.guild
          voice_channel = server.voice_client
          async with ctx.typing():
              filename = await YTDLSource.from_url(url, loop=self.bot.loop)
              voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
          await ctx.send('**Now playing:** {}'.format(filename))
      except Exception as e:
          await ctx.send(f"The bot is not connected to a voice channel.\n\nException: {e}")




























def setup(bot):
  bot.add_cog(Music(bot))