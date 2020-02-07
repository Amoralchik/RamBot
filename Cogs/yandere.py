import functools
import itertools
import math
import asyncio
import discord
import youtube_dl
import os
import requests
import random
from bs4 import BeautifulSoup
from discord.ext import commands , tasks
from itertools import cycle

def parser(tagsite, tag = None):

    if tag != None:

        tagr = requests.get(tagsite, params= tag)

    else:
        tagr = requests.get(tagsite)
        
    tagsoup = BeautifulSoup(tagr.content, "lxml")

    tagulid = tagsoup.find("ul", attrs={"id":"post-list-posts"})
    tagdivs = tagulid.find_all("a", attrs={"class":"thumb"})

    randomlink = random.choice(tagdivs).get("href")

    site = ("https://yande.re" + randomlink)

    r = requests.get(site)
    soup = BeautifulSoup(r.content, "lxml")

    title = soup.find("img", attrs={"class":"image"})
    return title.get("src")

class yandere(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=["yanderetop1d"])
    async def Yanderetop1d(self, ctx):

        if ctx.channel.is_nsfw():

            topsite = "https://yande.re/post/popular_recent?period=1d"
            
            emb = discord.Embed(colour=discord.Colour.magenta())
            emb.set_image(url= (parser(topsite)))
            emb.set_author(name= "yande.re url", url=topsite)
            emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

            await ctx.send(embed= emb)

        else:

            await ctx.send("only on NSFW channel")

    @commands.command(aliases=["yanderetop1w"])
    async def Yanderetop1w(self, ctx):

        if ctx.channel.is_nsfw():

            topsite = "https://yande.re/post/popular_recent?period=1w"
            
            emb = discord.Embed(colour=discord.Colour.magenta())
            emb.set_image(url= (parser(topsite)))
            emb.set_author(name= "yande.re url", url=topsite)
            emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

            await ctx.send(embed= emb)

        else:

            await ctx.send("only on NSFW channel")

    @commands.command(aliases=["yanderetop1m"])
    async def Yanderetop1m(self, ctx):

        if ctx.channel.is_nsfw():

            topsite = "https://yande.re/post/popular_recent?period=1m"
            
            emb = discord.Embed(colour=discord.Colour.magenta())
            emb.set_image(url= (parser(topsite)))
            emb.set_author(name= "yande.re url", url=topsite)
            emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

            await ctx.send(embed= emb)

        else:

            await ctx.send("only on NSFW channel")

    @commands.command(aliases=["yanderetop1y"])
    async def Yanderetop1y(self, ctx):

        if ctx.channel.is_nsfw():

            topsite = "https://yande.re/post/popular_recent?period=1y"
            
            emb = discord.Embed(colour=discord.Colour.magenta())
            emb.set_image(url= (parser(topsite)))
            emb.set_author(name= "yande.re url", url=topsite)
            emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

            await ctx.send(embed= emb)

        else:

            await ctx.send("only on NSFW channel")
    
    @commands.command(aliases=["yanderetag"])
    async def Yanderetag(self, ctx, *arg):

        tagsite = ("https://yande.re/post")

        if ctx.channel.is_nsfw():

            payload = {"tags" : f"-rating:s " + "+".join(arg)}

        else:
            
            payload = {"tags" : f"rating:s " + "+".join(arg)}

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.set_image(url= parser(tagsite, payload))
        emb.set_author(name= "yande.re url", url= parser(tagsite, payload))
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["yanderenew"])
    async def Yanderenew(self, ctx):

        tagsite = "https://yande.re/post"

        if ctx.channel.is_nsfw():

            payload = {"tags" : "-rating:s"}

        else:

            payload = {"tags" : "rating:s"}

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.set_image(url= parser(tagsite, payload))
        emb.set_author(name= "yande.re url", url= parser(tagsite, payload))
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["yanderelast"])
    async def Yanderelast(self, ctx):

        if ctx.channel.is_nsfw():

            payload = {"tags" : "-rating:s"}

        else:

            payload = {"tags" : "rating:s"}

        site = requests.get("https://yande.re/post", params=payload)
        linksoup = BeautifulSoup(site.content, "lxml")

        linkdivs = linksoup.find("a", attrs={"class":"thumb"})

        linksite = ("https://yande.re" + linkdivs.get("href"))

        r = requests.get(linksite)
        soup = BeautifulSoup(r.content, "lxml")

        title = soup.find("img", attrs={"class":"image"})["src"]

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.set_image(url= title)
        emb.set_author(name= "yande.re url", url=linksite)
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command(aliases=["yandererandom"])
    async def Yandererandom(self, ctx):
        
        if ctx.channel.is_nsfw():
        
            site = ("https://yande.re/post/random")

            r = requests.get(site)
            soup = BeautifulSoup(r.content, "lxml")

            divs = soup.find_all("div", attrs={"class":"content"})
            for div in divs:
                title = div.find("img", attrs={"class":"image"})["src"]
            
            emb = discord.Embed(colour=discord.Colour.magenta())
            emb.set_image(url= title)
            emb.set_author(name= "yande.re url", url=r.url)
            emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

            await ctx.send(embed= emb)
        
        else:
        	await ctx.send("only on NSFW channel")

def  setup(client):
	client.add_cog(yandere(client))