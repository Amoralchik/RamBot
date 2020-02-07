import functools
import itertools
import math
import asyncio
import discord
import youtube_dl
import os
import random
import datetime
import json
from datetime import datetime
from discord.ext import commands , tasks
from itertools import cycle
from discord import Spotify, Game, Streaming, CustomActivity

class info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None 

    @commands.command(aliases=["help"], error= "ctx error")
    async def Help(self, ctx):

        emb = discord.Embed(title= (f"{self.bot.user.name}"), url= "https://discordapp.com/oauth2/authorize?client_id=308615211462426625&permissions=8&scope=bot" ,colour=discord.Colour.magenta())
        emb.add_field(name= "✨Admin", value= "• setprefix \n • delete")
        emb.add_field(name= "❓8Ball", value= "• Yesornot \n • 8ball \n • choose")
        emb.add_field(name= "🗺Info", value= "• Version \n • ping \n • emojis \n • serverinfo \n • userinfo \n • avatar")
        emb.add_field(name= "💕RP", value= "• Hug \n • Put \n • Kiss \n • Triggered \n • Thinking \n • Fight \n • Angry \n • Cry")
        emb.add_field(name= "🎨Yandere", value= "• yanderetag \n • yanderenew \n • yanderelast \n • yandererandom \n • yanderetop1d \n • yanderetop1w \n • yanderetop1m \n • yanderetop1y")
        emb.add_field(name= "Other", value= "• Amo \n • help \n • Povtor \n • yes")
        emb.add_field(name= "🎶Music", value= "• join \n • leave \n • loop \n • now \n • pause \n • play \n • queue \n • remove \n • resume \n • shuffle \n • skip \n • stop \n • summon \n • volume")
        emb.add_field(name= "Bot info", value= "• Created by <@306125994396483587> \n • Version: 0.95 \n • Music by Valentin B.")
        emb.set_thumbnail(url= self.bot.user.avatar_url_as(static_format='png'))
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)
        
        await ctx.send( embed= emb )

    @commands.command(aliases=["version", "vrs"], brief= "Version info", error= "ctx error")
    async def Version(self, ctx):
        """ "версия","Версия","vrs" показывает текушую версию бота"""

        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Version", value= "0.94")
        emb.add_field(name= "Last Update", value= "04/02/2020")
        emb.set_footer(text= "Requested by {}".format(ctx.author.name), icon_url= ctx.author.avatar_url)
        
        await ctx.send( embed= emb )

	#Показывает пинг
    @commands.command(aliases=["ping"], brief= "Ping info", error= "ctx error")
    async def Ping(self, ctx):
        
        emb = discord.Embed(colour=discord.Colour.magenta())
        emb.add_field(name= "Ping", value= (f"Pong: {(round(self.bot.latency * 1000))}ms"))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)
    
    @commands.command(aliases=["emojis"], brief= "Emoji info", error= "ctx error")
    async def Emojis(self, ctx, guild: discord.Guild = None):
        """ Server Emoji """

        guild = guild or ctx.guild

        emojislist = [str(x) for x in guild.emojis]

        emb = discord.Embed(colour=discord.Colour.magenta())

        emb.add_field(name= "Emojis", value= str(len(guild.emojis)) + " : " +  " | ".join(emojislist) )
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)

    @commands.command(aliases=["serverinfo"], brief= "Server info", error= "ctx error")
    async def Serverinfo(self, ctx, guild: discord.Guild = None):
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
        emb.set_thumbnail(url= guild.icon_url_as(static_format='png'))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)

    @commands.command(aliases=["userinfo"], brief= "User info", error= "ctx error")
    async def Userinfo(self, ctx, member: discord.Member = None):
        """ Информация о пользователе """

        discord.User = member or ctx.author
        member = member or ctx.author

        rolelist = ([roles.name for roles in member.roles])
        activitiesname = ([activities.name for activities in member.activities])

        emb = discord.Embed(title= "Info about {}".format(member.name), colour=discord.Colour.magenta())
        emb.add_field(name= "Сreated", value= str(discord.User.created_at)[:16])

        if member.display_name == member.name:
            pass
        else:
            emb.add_field(name= "Server name", value= " ** " + member.display_name + " ** ")
           
        emb.add_field(name= "Joined at", value= str(member.joined_at)[:16])
        emb.add_field(name= "ID", value= member.id)
        emb.add_field(name= "Status", value= member.status)
        
        if str(activitiesname) != "[]":    
            for activity in member.activities:
                
                if isinstance(activity, Streaming):
                    emb.add_field(name= "Streaming", value=f"{member} is streaming it {activity.name} \n  {activity.url}", inline = False)

                if isinstance(activity, Spotify):
                    emb.add_field(name= "Listen", value= f"** {activity.title} ** by ** {activity.artists[0]} **", inline = False)

                if isinstance(activity, Game):
                    emb.add_field(name= "Game", value= f" playing to ** {activity.name} **", inline = False)

                if isinstance(activity, CustomActivity):
                    emb.add_field(name= "Custom Status", value= f"{activity.emoji} ** {activity.name} **")
        else:
            pass

        emb.add_field(name= "Roles", value= str(len(rolelist)) + " : " +   " | ".join(rolelist), inline = False)
        emb.set_thumbnail(url= member.avatar_url_as(static_format='png'))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)

    @commands.command(aliases=["avatar"], brief= "User avatar", error= "ctx error")
    async def Avatar(self, ctx, user: discord.User = None):
        """ Показывает аватар пользывателя """
        
        user = user or ctx.author
        
        emb = discord.Embed(title= "Avatar: {}".format(user.name), colour=discord.Colour.magenta())
        emb.set_image(url= user.avatar_url_as(static_format='png'))
        emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)
        
        await ctx.send(embed= emb)


def  setup(client):
	client.add_cog(info(client))