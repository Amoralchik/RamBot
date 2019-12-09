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
	# уже работает, и говорит привет на привет =_=

		if message.content == 'Привет рам':
			await message.channel.send("Привет няш <:lewd:443438908697739274>")
		elif message.content == 'Привет Рам':
			await message.channel.send("Привет няш <:lewd:443438908697739274>")
		elif message.content == 'Привет Рам чян':
			await message.channel.send("Привет няш <:lewd:443438908697739274>")
		elif message.content == 'Привет рам чян':
			await message.channel.send("Привет няш <:lewd:443438908697739274>")
		elif message.content == 'привет рам':
			await message.channel.send("Привет няш <:lewd:443438908697739274>")
		elif message.content == 'привет рам чян':
			await message.channel.send("Привет няш <:lewd:443438908697739274>")

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
		await ctx.send(f"{random.choice(Yesornot)}")

	@commands.command(aliases=["Megi"])
	async def megi(self, ctx,):
		""" "megi" """
		await ctx.send(f"<:mugi1:652603865069518848><:mugi2:652603713801682976><:mugi3:652603701239873623>")
		
	@commands.command()
	async def Povtor(self, ctx, *, arg):
		await ctx.send(arg)

def  setup(client):
	client.add_cog(Hi(client))