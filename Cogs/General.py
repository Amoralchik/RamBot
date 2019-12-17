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

	def __init__(self, bot, Version):
		self.bot = bot
		self._last_member = None

	@commands.command(aliases=["Delete","d"])
	@commands.has_permissions(administrator = True)
	async def delete(self, ctx, amount: int):
		""" УДАЛЯЕТ ВЫБРАННОЕ КОЛИЧЕСТВО СООБЩЕНИЙ """
		await ctx.channel.purge(limit= amount)
		await ctx.send("Удаленно " + str(amount) + " сообщений <:LewdMegumin:656439081747873802>")

	#Показывает пинг
	@commands.command(aliases=["Пинг","пинг"])
	async def ping(self, ctx):
		""" "Пинг","пинг" Показывает Пинг"""
		if self.bot.latency * 1000 >= 150:
			await ctx.send(f"пинг: {(round(self.bot.latency * 1000))}ms <:remhmpf:652885984115163196> ")
		elif self.bot.latency * 1000 <= 100:
			await ctx.send(f"<:RamKiss:656439218733580309> пинг: {(round(self.bot.latency * 1000))}ms ")
		elif self.bot.latency * 1000 <= 150:
			await ctx.send(f"пинг: {(round(self.bot.latency * 1000))}ms <:RamOwO:656438972284796928> ")

	#показывает версию бота.
	@commands.command(aliases=["версия","Версия","vrs"])
	async def Vrs(self, ctx):
		""" "версия","Версия","vrs" показывает текушую версию бота"""
		await ctx.send(f"<:RamKiss:656439218733580309> Версия: 0.60 // дата последнего обновления 17/12/2019 <:RemKiss:656439154225315850>")

	#команда про меня
	@commands.command(aliases=["Amo","amo","амо"])
	async def Амо(self, ctx):
		if ctx.message.author.id == 306125994396483587:
			await ctx.send('Амо Амо Аморальчик <:RemKiss:656439154225315850>')
		else:
			await ctx.send('Ты не Аномальчик')

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			await ctx.send("Извини няш, но что то пошло не так...<:smugram:656439012352983041>")


def  setup(client):
	client.add_cog(General(client))
