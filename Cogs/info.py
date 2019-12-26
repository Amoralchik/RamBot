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

    @commands.command(aliases=["версия","Версия","vrs"])
    async def Vrs(self, ctx, user: discord.User = None):
        user = user or ctx.author
        """ "версия","Версия","vrs" показывает текушую версию бота"""
        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Версия", value= "Версия: 0.85")
        emb.add_field(name= "Дата последнего обновления", value= "23/12/2019")
        emb.add_field(name= "Github", value= "https://github.com/Amoralchik/RamBot")
        emb.set_footer(text= "Сaused by {}".format(user.name), icon_url= user.avatar_url)
        await ctx.send( embed= emb )

    @commands.command(aliases=[])
    async def test(self, ctx, user: discord.User = None):
        user = user or ctx.author
        emb = discord.Embed(title= "Info about {}".format(user.name), colour=discord.Colour.magenta())
        emb.add_field(name= "Name", value= user.name)
        emb.add_field(name= "Сreated", value= str(user.created_at)[:16])
        if user.display_name == user.name:
            pass
        elif user.display_name !=  user.name:
            emb.add_field(name= "Server name", value= user.display_name)
        emb.add_field(name= "Joined at", value= str(user.joined_at)[:16])
        emb.add_field(name= "ID", value= user.id)
        emb.set_thumbnail(url= user.avatar_url_as(format='png'))
        emb.set_footer(text= "Сaused by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        await ctx.send(embed= emb)

	#Показывает пинг
    @commands.command(aliases=["Пинг", "пинг"])
    async def ping(self, ctx):
        """ "Пинг", "пинг" Показывает Пинг"""
        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Ping", value= (f"понг: {(round(self.bot.latency * 1000))}ms"))
        emb.set_footer(text= "Сaused by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        await ctx.send(embed= emb)

    @commands.command(pass_context= True)
    async def serverinfo(self, ctx, guild: discord.Guild = None):
        guild = guild or ctx.guild
        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Server name", value= str(guild.name))
        emb.add_field(name= "ID", value= guild.id)
        emb.add_field(name= "Region", value= guild.region)
        emb.add_field(name= "Text channels", value= ([channels.name for channels in guild.text_channels]))
        emb.add_field(name= "Voice channels", value= ([channels.name for channels in guild.voice_channels]))
        emb.add_field(name= "Members", value= ([member.name for member in guild.members]))
        emb.add_field(name= "Roles", value= ([roles.name for roles in guild.roles]))
        emb.add_field(name= "Owner", value= guild.owner)
        emb.set_thumbnail(url= guild.icon_url_as(format='png'))
        emb.set_footer(text= "Сaused by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        await ctx.send(embed= emb)

    @commands.command(pass_context= True)
    async def info(self, ctx, member: discord.Member = None):
        """ Информация о пользователе """
        discord.User = member or ctx.author
        member = member or ctx.author
        emb = discord.Embed(title= "Info about {}".format(member.name), colour=discord.Colour.magenta())
        emb.add_field(name= "Name", value= member.name)
        emb.add_field(name= "Сreated", value= str(discord.User.created_at)[:16])
        if member.display_name == member.name:
            pass
        elif member.display_name !=  member.name:
            emb.add_field(name= "Server name", value= member.display_name)
        emb.add_field(name= "Joined at", value= str(member.joined_at)[:16])
        emb.add_field(name= "ID", value= member.id)
        emb.set_thumbnail(url= member.avatar_url_as(format='png'))
        emb.set_footer(text= "Сaused by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        await ctx.send(embed= emb)

    @commands.command(pass_context= True)
    async def avatar(self, ctx, user: discord.User = None):
        """ Показывает аватар пользывателя """
        user = user or ctx.author
        emb = discord.Embed(title= "Avatar: {}".format(user.name), colour=discord.Colour.magenta())
        emb.set_image(url= user.avatar_url_as(format='png'))
        emb.set_footer(text= "Сaused by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        await ctx.send(embed= emb)


def  setup(client):
	client.add_cog(info(client))