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

class yandere(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def tag_yandere(self, ctx, *arg):

        tagsite = ("https://yande.re/post")
        payload = {"tags" : arg}
        tagr = requests.get(tagsite, params=payload)
        tagsoup = BeautifulSoup(tagr.content, "html.parser")

        tagulid = tagsoup.find("ul", attrs={"id":"post-list-posts"})
        tagdivs = tagulid.find_all("a", attrs={"class":"thumb"})

        randomlink = random.choice(tagdivs).get("href")

        site = ("https://yande.re" + randomlink)

        r = requests.get(site)
        soup = BeautifulSoup(r.content, "html.parser")

        divs = soup.find_all("div", attrs={"class":"content"})
        for div in divs:
            title = div.find("img", attrs={"class":"image"})["src"]

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.set_image(url= title)
        emb.set_author(name= "yande.re url", url=site)
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command()
    async def new_yandere(self, ctx):

        site = ("https://yande.re/post")

        linkr = requests.get(site)
        linksoup = BeautifulSoup(linkr.content, "html.parser")

        linkdivs = linksoup.find_all("a", attrs={"class":"thumb"})

        randomlink = random.choice(linkdivs).get("href")

        linksite = ("https://yande.re" + randomlink)

        r = requests.get(linksite)
        soup = BeautifulSoup(r.content, "html.parser")

        title = soup.find("img", attrs={"class":"image"})["src"]

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.set_image(url= title)
        emb.set_author(name= "yande.re url", url=linksite)
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command()
    async def last_yandere(self, ctx):

        site = ("https://yande.re/post")

        linkr = requests.get(site)
        linksoup = BeautifulSoup(linkr.content, "html.parser")

        linkdivs = linksoup.find("a", attrs={"class":"thumb"})

        linksite = ("https://yande.re" + linkdivs.get("href"))

        r = requests.get(linksite)
        soup = BeautifulSoup(r.content, "html.parser")

        title = soup.find("img", attrs={"class":"image"})["src"]

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.set_image(url= title)
        emb.set_author(name= "yande.re url", url=linksite)
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

    @commands.command()
    async def random_yandere(self, ctx):

        site = ("https://yande.re/post/random")

        r = requests.get(site)
        soup = BeautifulSoup(r.content, "html.parser")

        divs = soup.find_all("div", attrs={"class":"content"})
        for div in divs:
            title = div.find("img", attrs={"class":"image"})["src"]
            
        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.set_image(url= title)
        emb.set_author(name= "yande.re url", url=r.url)
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)

        await ctx.send(embed= emb)

def  setup(client):
	client.add_cog(yandere(client))