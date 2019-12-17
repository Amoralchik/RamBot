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
	async def on_message(self, message, my_str='привет рам'):

		if "привет рам" in message.content.lower():
			await message.channel.send("Привет няш <:RamOwO:656438972284796928>")
		elif message.author.id == 306125994396483587 and "Тоша бака" in message.content.lower() :
			await message.channel.send("дя, тоша бяка <:remhmpf:652885984115163196>")

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
			await ctx.send('Привет {0.name}~'.format(member))
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
