import discord
from discord.ext import commands
from datetime import datetime

class levelsystem(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.leveldata = {}

  @commands.Cog.listener()
  async def on_ready(self):
    dict = {}
    guild = self.client.get_guild(884093430857363536)
    for channel in guild.channels:
      print("Habibi, Za Leveling System Is Online")
      messages = [message async for message in channel.history(after=datetime.today().replace(day=1))]
      for x in messages:
        if x.author.id in dict:
          dict[x.author.id] = dict[x.author.id] + 1
        else:
          dict[x.author.id] = 1
      
    temp = sorted(dict.items(), key = lambda x: x[1])
    for i in range(len(temp)):
      self.leveldata[temp[i][0]] = temp[i][1]
    print("it's done Habibi")

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.id in self.leveldata:
      self.leveldata[message.author.id] = self.leveldata[message.author.id] + 1
    else:
      self.leveldata[message.author.id] = 1
  

  @commands.command()
  async def rank(self,ctx):
    temp = sorted(self.leveldata.items(), key = lambda x: x[1])
    self.leveldata = {}
    for i in range(len(temp)):
      self.leveldata[temp[i][0]] = temp[i][1]
    if ctx.author.id in self.leveldata:
      xp = self.leveldata[ctx.author.id]
      rank = list(self.leveldata).index(ctx.author.id)
      xp *= 5
      lvl = 0
      while True:
        if xp < ((50 * (lvl**2)) + (50* lvl)):
          break
        lvl +=1
      xp -= ((50 * ((lvl-1)**2)) + (50* (lvl-1)))
      boxes = int((xp / (200 * ((1/2) * (lvl))) * 20))
      embed = discord.Embed(title = "Brazer {}'s level stats".format(ctx.author.name), description="", color= 0x397882)
      embed.add_field(name="Name", value=ctx.author.mention, inline=True)
      embed.add_field(name="XP", value=f"{xp}/{int(200 *(1/2) *lvl)}", inline=True)
      embed.add_field(name="Level", value=lvl, inline=True)
      embed.add_field(name="Rank", value=f"{rank+1}/{ctx.guild.member_count}", inline=True)
      embed.add_field(name="Progress Bar [lvl]", value=boxes*":red_square:" + (20-boxes) * ":white_large_square:", inline=False)
      embed.set_thumbnail(url=ctx.author.display_avatar)
      await ctx.channel.send(embed=embed)
    else:
      await ctx.channel.send("Habibi, You have no rank.")

async def setup(client):
  await client.add_cog(levelsystem(client))