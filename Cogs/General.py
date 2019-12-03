import discord
import os
import random
from discord.ext import commands

class General(commands.Cog):
#Класс 3
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	#Показывает пинг
	@commands.command(aliases=["Пинг","пинг"])
	async def ping(self, ctx,):
		""" "Пинг","пинг" Показывает Пинг"""
		await ctx.send(f"пинг: {(round(self.bot.latency * 1000))}ms <:lewd:443438908697739274>")

	#показывает версию бота.
	@commands.command(aliases=["версия","Версия","version","vrs"])
	async def Vrs(self, ctx,):
		""" "версия","Версия","version","vrs" показывает текушую версию бота"""
		await ctx.send(f"Верисия: 00.17 Альфа // дата последнего обновления 31/11/2019 <:NICE:443438905027461150>")

	#команда про меня
	@commands.command(aliases=["Amo","amo"])
	async def Амо(self, ctx):
		"""	"Amo","amo" аморальчик"""
		Amoral = ["Амо Амо", "Амо Амо Аморал", "Аморальчик", "Аномальчик","Мой маленький создатель","Мой повелитель =^_^="]
		await ctx.send(f"{random.choice(Amoral)}")

def  setup(client):
	client.add_cog(General(client))