import functools
import itertools
import math
import asyncio
import discord
import youtube_dl
import os
import random
from discord.ext import commands , tasks
from itertools import cycle

class Rp(commands.Cog):
    #Класс 1
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        """Kiss"""
        author = ctx.author.mention
        mention = member.mention
        
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'http://i.imgur.com/TNhivqs.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif']
        
        image = random.choice(choices)
        
        emb = discord.Embed(description="**{0} gave {1} a kiss!**".format(author, mention), colour=discord.Colour.magenta())
        emb.set_image(url=image)

        await ctx.send(embed= emb)


    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        """Pat"""
        author = ctx.message.author.mention
        mention = member.mention
        
        pat = "**{0} got patted by {1}!**"
        
        choices = ['http://i.imgur.com/10VrpFZ.gif', 'http://i.imgur.com/x0u35IU.gif', 'http://i.imgur.com/0gTbTNR.gif', 'http://i.imgur.com/hlLCiAt.gif', 'http://i.imgur.com/sAANBDj.gif']
        
        image = random.choice(choices)
        
        emb= discord.Embed(description=pat.format(mention, author), colour=discord.Colour.magenta()())
        emb.set_image(url=image)

        await ctx.send(embed= emb)

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        """Hug"""
        author = ctx.message.author.mention
        mention = member.mention
        
        hug = "**{0} gave {1} a hug!**"
        
        choices = ['http://i.imgur.com/sW3RvRN.gif', 'http://i.imgur.com/gdE2w1x.gif', 'http://i.imgur.com/zpbtWVE.gif', 'http://i.imgur.com/ZQivdm1.gif', 'http://i.imgur.com/MWZUMNX.gif']
        
        image = random.choice(choices)
        
        emb = discord.Embed(description=hug.format(author, mention), colour=discord.Colour.magenta()())
        emb.set_image(url=image)

        await ctx.send(embed= emb)


def  setup(client):
	client.add_cog(Rp(client))
