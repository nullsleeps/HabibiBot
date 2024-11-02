import discord
from discord.ext import commands
import pyjokes
import asyncio
import os
import random

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Habibi, Za Fun System Is Online")
    
    @commands.command()
    async def bing(self, ctx):
     brazer_embed = discord.Embed(title="Habibi", description="Here iz my bing", color=discord.Color.orange())
     brazer_embed.add_field(name=f"{self.bot.user.name}'s Habibi Per Second: ", value=f"{round(self.bot.latency * 1000)} HabibiPerSecond", inline=False)
     brazer_embed.set_footer(text="Hello my Brazer", icon_url=self.bot.user.avatar)
     await ctx.send(embed=brazer_embed)

    @commands.command()
    async def yalla(self, ctx):
     await ctx.send('HABIBII')

    @commands.command()
    async def joke(self, ctx):
     joke = pyjokes.get_joke()
     await ctx.send(joke)

    @commands.command(aliases=["HELP", "Help", "Ambulance", "call 911"])
    async def medicalhelp(self, ctx):
     await ctx.send(f"Habibi, {ctx.author.mention} Shatup before I make za medical broblem 100 timez worze")

    @commands.command(name="9/11" "911")
    async def september11th2001(self, ctx):
     await ctx.send("Oh, Zats My favourite Holiday")

    @commands.command(name="hi" "Hi" "Helllo" "hello")
    async def welcome(self, ctx):
     habibilist = ["Hello Brazer" "Hi Habibi" "HELLO HABIBI HOW ARE YOU"]
     await ctx.send(habibilist)

async def setup(bot):
   await bot.add_cog(fun(bot))