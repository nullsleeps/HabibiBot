import discord
from discord.ext import commands, tasks
import asyncio
import os
from random import choice
import asyncpraw as praw

class redditmemes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = praw.Reddit(client_id="CdQ7E_27esJHgfseu0OSBw", client_secret="6jMmCpccSWy4Qy5V5CQBNU6OLCKBkA", user_agent="script:random:v1.0 (by u/s3nl)")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Habibi, Za Meme System iz Online")

    @commands.command()
    async def meme(self, ctx: commands.Context):
        subreddit = await self.reddit.subreddit("memes")
        posts_list = []
        async for post in subreddit.new(limit=40):
            if post.author is not None and any(post.url.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".gif"]):
                author_name = post.author.name
                posts_list.append((post.url, author_name))
            if post.author is None:
                posts_list.append((post.url, "N/A"))

        if posts_list: 
            random_post = choice(posts_list)
            meme_embed = discord.Embed(title="Memez", description="MEMEMES", color=discord.Color.random())
            meme_embed.set_author(name=f"Brazer, This Subid Bost waz Requested by {ctx.author.name}- You are my brazer", icon_url=ctx.author.avatar)
            meme_embed.set_image(url=random_post[0])
            meme_embed.set_footer(text=f"Habibi, Zis Crazy Bost waz created by {random_post[1]} - He is alzo my brazer", icon_url=None)
            await ctx.send(embed=meme_embed)
        else:
            await ctx.send("Unable to get mememe")
        if subreddit:
            await self.reddit.subreddit("memes")
        else:
            subreddit.close()




def cog_unload(self):
 self.bot.loop.create_task(self.reddit.close())
async def setup(bot):
   await bot.add_cog(redditmemes(bot))