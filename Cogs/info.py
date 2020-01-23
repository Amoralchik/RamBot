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
    async def Version(self, ctx, user: discord.User = None):
        """ "версия","Версия","vrs" показывает текушую версию бота"""

        user = user or ctx.author

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Version", value= "Версия: 0.91")
        emb.add_field(name= "Last Update", value= "23/01/2020")
        emb.add_field(name= "Github", value= "https://github.com/Amoralchik/RamBot" inline=False)
        emb.set_footer(text= "Requested by {}".format(user.name), icon_url= user.avatar_url)
        
        await ctx.send( embed= emb )

	#Показывает пинг
    @commands.command(aliases=["Пинг", "пинг"])
    async def ping(self, ctx):
        """ "Пинг", "пинг" Показывает Пинг"""
        
        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Ping", value= (f"Pong: {(round(self.bot.latency * 1000))}ms"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)
    
    @commands.command(pass_context=True)
    async def emojis(self, ctx, guild: discord.Guild = None):
        """ Server Emoji """

        guild = guild or ctx.guild

        emojislist = [str(x) for x in guild.emojis]

        emb = discord.Embed(colour=discord.Colour.magenta())

        emb.add_field(name= "Emojis", value= str(len(guild.emojis)) + " : " +  " | ".join(emojislist) )
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)

    @commands.command(pass_context= True)
    async def serverinfo(self, ctx, guild: discord.Guild = None):
        """ Информация о Сервере """
        
        guild = guild or ctx.guild

        textlist = ([channels.name for channels in guild.text_channels])
        voiclist = ([channels.name for channels in guild.voice_channels])
        memberlist = ([member.name for member in guild.members])
        rolelist = ([roles.name for roles in guild.roles])

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Server name", value= str(guild.name))
        emb.add_field(name= "ID", value= guild.id, inline= True)
        emb.add_field(name= "Region", value= guild.region)
        emb.add_field(name= "Text channels", value= str(len(textlist)) + " : " +  " | ".join(textlist) , inline=False)
        emb.add_field(name= "Voice channels", value= str(len(voiclist)) + " : " +  " | ".join(voiclist) , inline=False)
        emb.add_field(name= "Members", value= str(len(memberlist)) + " : " +  " | ".join(memberlist) , inline=False)
        emb.add_field(name= "Roles", value= str(len(rolelist)) + " : " +  " | ".join(rolelist)  , inline=False)
        emb.add_field(name= "Owner", value= guild.owner)
        emb.set_thumbnail(url= guild.icon_url_as(format='png'))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)

    @commands.command(pass_context= True)
    async def userinfo(self, ctx, member: discord.Member = None):
        """ Информация о пользователе """

        discord.User = member or ctx.author
        member = member or ctx.author

        rolelist = ([roles.name for roles in member.roles])
        activitiesname = ([activities.name for activities in member.activities])

        emb = discord.Embed(title= "Info about {}".format(member.name), colour=discord.Colour.magenta())
        emb.add_field(name= "Name", value= member.name)
        emb.add_field(name= "Сreated", value= str(discord.User.created_at)[:16])

        if member.display_name == member.name:
            pass
        elif member.display_name !=  member.name:
            emb.add_field(name= "Server name", value= member.display_name)

        emb.add_field(name= "Joined at", value= str(member.joined_at)[:16])
        emb.add_field(name= "ID", value= member.id)
        emb.add_field(name= "Activities", value= " ".join(activitiesname))
        emb.add_field(name= "Status", value= member.status)
        emb.add_field(name= "Roles", value= str(len(rolelist)) + " : " +   " | ".join(rolelist) )
        emb.add_field(name= "Status", value= member.status)
        emb.set_thumbnail(url= member.avatar_url_as(static_format='png'))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)

    @commands.command(pass_context= True)
    async def avatar(self, ctx, user: discord.User = None):
        """ Показывает аватар пользывателя """
        
        user = user or ctx.author
        
        emb = discord.Embed(title= "Avatar: {}".format(user.name), colour=discord.Colour.magenta())
        emb.set_image(url= user.avatar_url_as(static_format='png'))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)


def  setup(client):
	client.add_cog(info(client))