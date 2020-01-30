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
		
		if message.author.id == 306125994396483587 and "привет амо" in message.content.lower():
			await message.channel.send("Привет Аморальчик <:RemKiss:656439154225315850>")
		elif message.author.id == 311255280442933248 and "привет амо" in message.content.lower():
			await message.channel.send("Привет Анишечка <:NICE:443438905027461150>")
		elif message.author.id == 419066289298997250 and "привет амо" in message.content.lower():
			await message.channel.send("Привет Ддешка <:RamOwO:656438972284796928>")
		elif message.author.id == 279550029981548545 and "привет амо" in message.content.lower():
			await message.channel.send("Привет Тошик <:RamOwO:656438972284796928>")
		elif message.author.id == 272318540722339840 and "привет амо" in message.content.lower():
			await message.channel.send("Привет Вуф вуф вульфик <:RamOwO:656438972284796928>")
		elif message.author.id == 270937744455237632 and "привет амо" in message.content.lower():	
			await message.channel.send("Привет Вельзик <:RamOwO:656438972284796928>")
		elif (message.author.id != 270937744455237632, 311255280442933248, 419066289298997250, 279550029981548545, 272318540722339840) and "привет рам" in message.content.lower():
			await message.channel.send("Привет няш <:RamOwO:656438972284796928>")
		elif message.author.id == 306125994396483587 and "аморал бака" in message.content.lower():
			await message.channel.send("дя! <:LewdMegumin:656439081747873802> ")
		elif message.author.id == 306125994396483587 and "тоша бака" in message.content.lower():
			await message.channel.send("дя! <:remhmpf:652885984115163196>")
		elif message.author.id == 306125994396483587 and "рам и рем" in message.content.lower():	
			await message.channel.send("<:RamKiss:656439218733580309> <:RemKiss:656439154225315850>")

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send('Приветик {0.mention}.'.format(member))

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send('Пока :( {0.mention}.'.format(member))
			
	#простая команда вывода да/нет
	@commands.command(aliases=["+","yes","lf","да","Да"])
	async def Yes(self, ctx,):
		""" "+","yes","lf","да","Да" """
		Yes = ["Да","+"]
		await ctx.send(f"{random.choice(Yes)}")

	@commands.command(aliases=["povtor", "Повтор", "повтор"])
	async def Povtor(self, ctx, *, arg,):
		""" "povtor", "Повтор", "повтор" """
		await discord.Message.delete(ctx.message)
		await ctx.send(arg)

def  setup(client):
	client.add_cog(Hi(client))
