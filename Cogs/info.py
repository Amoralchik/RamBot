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
import datetime

class info(commands.Cog):
    #Класс 1
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(pass_context= True)
    async def info(self, ctx, user: discord.User = None):
        user = user or ctx.author
        emb = discord.Embed(title= "Info about {}".format(user.name), colour= 0xa200ff)
        emb.add_field(name= "Name", value= user.name)
        emb.add_field(name= "Сreated", value= str(user.created_at)[:16])
        if user.display_name == user.name:
            pass
        elif user.display_name !=  user.name:
            emb.add_field(name= "Server name", value= user.display_name)
        emb.add_field(name= "Joined at", value= str(user.joined_at)[:16])
        emb.add_field(name= "ID", value= user.id)
        emb.set_thumbnail(url= user.avatar_url)
        emb.set_footer(text= "Сaused by {}".format(user.name), icon_url= user.avatar_url)
        await ctx.send(embed= emb)

    @commands.command(pass_context= True)
    async def avatar(self, ctx, user: discord.User = None):
        user = user or ctx.author
        emb = discord.Embed(title= "Avatar: {}".format(user.name), colour= 0xa200ff)
        emb.set_image(url= user.avatar_url)
        await ctx.send(embed= emb)


def  setup(client):
	client.add_cog(info(client))