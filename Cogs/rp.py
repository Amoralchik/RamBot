import functools
import itertools
import math
import asyncio
import discord
import youtube_dl
import os
import random
import requests
import re
from bs4 import BeautifulSoup
from discord.ext import commands , tasks
from itertools import cycle

def randomgif(gifsite):

    site = requests.get(gifsite)
    linksoup = BeautifulSoup(site.content, "lxml")

    listtitle = []

    linkdivs = linksoup.find_all("figure", attrs={"class":"GifListItem"})
    for div in linkdivs:
        title = div.find("a", attrs={"activeclassname":"current"})["href"]
        listtitle.append(title)
    dlina_lista=len(listtitle)
    i=0
    while i<dlina_lista:
        if re.search(r'/gif-maker?utm_source=search-page&utm_medium=internal&utm_campaign=gif-maker-entrypoints', listtitle[i]):
            listtitle.pop([i])
        i+=1
    r= requests.get("https://tenor.com" + random.choice(listtitle))
    rsoup = BeautifulSoup(r.content, "lxml")

    rtitle = rsoup.find("div", attrs={"class":"Gif"})
    qtitle = rtitle.find("img")
    return qtitle.get("src")

class Rp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=["kiss"], error= "pls meniton member")
    async def Kiss(self, ctx, member: discord.Member):
        """Kiss"""
        author = ctx.author.mention
        mention = member.mention
        
        emb = discord.Embed(description="**{0} поцеловал {1}!**".format(author, mention), colour=discord.Colour.magenta())
        emb.set_image(url=randomgif("https://tenor.com/search/anime-kiss-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)


    @commands.command(aliases=["pat"], error= "pls meniton member")
    async def Pat(self, ctx, member: discord.Member):
        """Pat"""
        author = ctx.author.mention
        mention = member.mention
        
        emb= discord.Embed(description="**{0} похлопал {1} по голове!**".format(author, mention), colour=discord.Colour.magenta())
        emb.set_image(url=randomgif("https://tenor.com/search/anime-pat-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["angry"])
    async def Angry(self, ctx, member: discord.Member = None):
        author = ctx.author.mention
        
        if member == None:
            emb = discord.Embed(description="**{0} злится!**".format(author), colour=discord.Colour.magenta())

        else:

            mention = member.mention
            emb = discord.Embed(description="**{0} зол на {1}!**".format(author, mention), colour=discord.Colour.magenta())
        
        emb.set_image(url=randomgif("https://tenor.com/search/anime-angry-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)
    
    @commands.command(aliases=["cry"])
    async def Cry(self, ctx, member: discord.Member = None):
        author = ctx.author.mention
        
        if member == None:
            emb = discord.Embed(description="**{0} плачет!**".format(author), colour=discord.Colour.magenta())

        else:

            mention = member.mention
            emb = discord.Embed(description="**{0} плачет из за {1}!**".format(author, mention), colour=discord.Colour.magenta())
        
        emb.set_image(url=randomgif("https://tenor.com/search/anime-cry-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["fight"], error= "pls meniton member")
    async def Fight(self, ctx, member: discord.Member = None):
        author = ctx.author.mention
        mention = member.mention
        
        emb= discord.Embed(description="**{0} ударил {1}!**".format(author, mention), colour=discord.Colour.magenta())
        emb.set_image(url=randomgif("https://tenor.com/search/anime-fight-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["thinking"])
    async def Thinking(self, ctx, member: discord.Member = None):
        author = ctx.author.mention
        
        if member == None:
            emb = discord.Embed(description="**{0} задумался...**".format(author), colour=discord.Colour.magenta())

        else:

            mention = member.mention
            emb = discord.Embed(description="**{0} задумался из за {1}!**".format(author, mention), colour=discord.Colour.magenta())
        
        emb.set_image(url=randomgif("https://tenor.com/search/anime-thinking-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["triggered"])
    async def Triggered(self, ctx, member: discord.Member = None):
        author = ctx.author.mention
        
        if member == None:
            emb = discord.Embed(description="**{0} тригернулся**".format(author), colour=discord.Colour.magenta())

        else:

            mention = member.mention
            emb = discord.Embed(description="**{0} тригернулся на {1}!**".format(author, mention), colour=discord.Colour.magenta())
        
        emb.set_image(url=randomgif("https://tenor.com/search/anime-triggered-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["hug"], error= "pls meniton member")
    async def Hug(self, ctx, member: discord.Member):
        """Hug"""
        author = ctx.author.mention
        mention = member.mention
        
        emb = discord.Embed(description="**{0} обнял {1}!**".format(author, mention), colour=discord.Colour.magenta())
        emb.set_image(url=randomgif("https://tenor.com/search/anime-hug-gifs"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)


def  setup(client):
	client.add_cog(Rp(client))
