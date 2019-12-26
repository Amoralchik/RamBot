import functools
import itertools
import math
import asyncio
import discord
import youtube_dl
import os
import random
import json
from discord.ext import commands , tasks
from itertools import cycle

class Administrator(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def setprefix(self, ctx, prefix):
		"""Устанавливает префикс комманд бота, нельзя использовать упоминания/пробелы!"""
		with open("prefixes.json","r") as f:
			prefixes = json.load(f)
	
		prefixes[str(ctx.guild.id)] = prefix

		with open("prefixes.json","w") as f:
			json.dump(prefixes, f, indent=4)
        
		await ctx.send(f"Префихс изменнен на: {prefix}")

	@commands.command(aliases=["Delete","d"])
	@commands.has_permissions(administrator = True)
	async def delete(self, ctx, amount: int):
		""" Удаляет н количество сообщений (только для админов) """
		await ctx.channel.purge(limit= amount)
		await ctx.send("Удаленно " + str(amount) + " сообщений <:LewdMegumin:656439081747873802>")

	#команда про меня
	@commands.command(aliases=["Amo","amo","амо"])
	async def Амо(self, ctx):
		"""Только для аморала"""
		if ctx.message.author.id == 306125994396483587:
			await ctx.send('Амо Амо Аморальчик <:RemKiss:656439154225315850>')
		elif ctx.message.author.id == 419066289298997250:
			await ctx.send('Хватит дедешка! ты не Аморальчик <:remhmpf:652885984115163196>')
		else:
			await ctx.send('Ты не Аномальчик')

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandNotFound):
			await ctx.send("Извини няш, но что то пошло не так...<:smugram:656439012352983041>")


def  setup(client):
	client.add_cog(Administrator(client))
