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

class Hi(commands.Cog):
	#Класс 1
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.Cog.listener()
	async def on_message(self, message):
		
		if message.author.id == 306125994396483587 and "привет рам" in message.content.lower():
			await message.channel.send("Привет Аморальчик <:RemKiss:656439154225315850>")
		elif message.author.id == 311255280442933248 and "привет рам" in message.content.lower():
			await message.channel.send("Привет Анишечка <:NICE:443438905027461150>")
		elif message.author.id == 419066289298997250 and "привет рам" in message.content.lower():
			await message.channel.send("Привет Ддешка <:RamOwO:656438972284796928>")
		elif message.author.id == 279550029981548545 and "привет рам" in message.content.lower():
			await message.channel.send("Привет Тошик <:RamOwO:656438972284796928>")
		elif message.author.id == 272318540722339840 and "привет рам" in message.content.lower():
			await message.channel.send("Привет Вуф вуф вульфик <:RamOwO:656438972284796928>")
		elif message.author.id == 270937744455237632 and "привет рам" in message.content.lower():	
			await message.channel.send("Привет Вельзик <:RamOwO:656438972284796928>")
		elif not (message.author.id == 270937744455237632 or 306125994396483587 or 311255280442933248 or 419066289298997250 or 279550029981548545 or 272318540722339840) and "привет рам" in message.content.lower():
			await message.channel.send("Привет няш <:RamOwO:656438972284796928>")
		elif message.author.id == 306125994396483587 and "тоша бака" in message.content.lower():
			await message.channel.send("дя, тоша бяка <:remhmpf:652885984115163196>")
		elif message.author.id == 306125994396483587 and "рам и рем" in message.content.lower():	
			await message.channel.send("<:RamKiss:656439218733580309> <:RemKiss:656439154225315850>")

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send('Приветик {0.mention}.'.format(member))

	@commands.command(aliases=["Привет","привет"])
	async def hello(self, ctx, *, member: discord.Member = None):
		""" Отвечает приветом на привет """
		member = member or ctx.author
		if self._last_member is None or self._last_member.id != member.id:
			await ctx.send('Привет {0.name}'.format(member))
		else:
			await ctx.send('Привет {0.name}... Кажется ты уже это делал.'.format(member))
			self._last_member = member

	#простая команда вывода да/нет
	@commands.command(aliases=["+","yes","lf","да","Да"])
	async def Yes(self, ctx,):
		""" "+","yes","lf","да","Да" """
		Yes = ["Да","+"]
		await ctx.send(f"{random.choice(Yes)}")

	@commands.command(aliases=["Mugi"])
	async def mugi(self, ctx,):
		""" "mugi" """
		await ctx.send(f"<:mugi1:652603865069518848><:mugi2:652603713801682976><:mugi3:652603701239873623>")

	@commands.command(aliases=["povtor", "Повтор", "повтор"])
	async def Povtor(self, ctx, *, arg,):
		""" "povtor", "Повтор", "повтор" """
		await ctx.channel.purge(limit=1)
		await ctx.send(arg)

def  setup(client):
	client.add_cog(Hi(client))
