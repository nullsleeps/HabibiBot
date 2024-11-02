import discord
from discord.ext import commands, tasks
import random
import pyjokes
import asyncio
import os
from itertools import cycle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "habibi ", intents=discord.Intents.all())

status = cycle(["Hala Habibi", "YALLA HABIBI", "Drifting The 2002 Toyota Camry I stole from my fazer", "Bismillah", "Alhamdulilah"])

@tasks.loop(seconds=3600)
async def botstatus():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    print(f'Habibi me {bot.user} I am ready')
    botstatus.start()

with open("brazer.txt") as file:
    brazer = file.read()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(brazer)

asyncio.run(main())