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

class General(commands.Cog):
#Класс 3
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	#Показывает пинг
	@commands.command(aliases=["Пинг","пинг"])
	async def ping(self, ctx,):
		""" "Пинг","пинг" Показывает Пинг"""
		if self.bot.latency * 1000 >= 150:
			await ctx.send(f"пинг: {(round(self.bot.latency * 1000))}ms <:MeguSleep:651940278327836683>")
		elif self.bot.latency * 1000 <= 100: 
			await ctx.send(f"пинг: {(round(self.bot.latency * 1000))}ms <:lewd:443438908697739274>")
		elif self.bot.latency * 1000 <= 150:
			await ctx.send(f"пинг: {(round(self.bot.latency * 1000))}ms <:PepeHands:651939903923290132>")

	#показывает версию бота.
	@commands.command(aliases=["версия","Версия","version","vrs"])
	async def Vrs(self, ctx,):
		""" "версия","Версия","version","vrs" показывает текушую версию бота"""
		await ctx.send(f"Верисия: 0.050 // дата последнего обновления 06/12/2019 <:NICE:443438905027461150>")

	#команда про меня
	@commands.command(aliases=["Amo","amo","амо"])
	async def Амо(self, ctx):
		"""	"Amo","amo" аморальчик"""
		Amoral = ["Амо Амо", "Амо Амо Аморал", "Аморальчик", "Аномальчик","Мой маленький создатель","Мой повелитель =^_^="]
		await ctx.send(f"{random.choice(Amoral)}")

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			await ctx.send("Извини няш, но такой команды нету...")


def  setup(client):
	client.add_cog(General(client))