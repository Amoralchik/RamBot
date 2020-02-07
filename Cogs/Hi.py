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

	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.Cog.listener()
	async def on_message(self, message):
					
		if "привет амо" in message.content.lower():
			await message.channel.send("Привет " + message.author.name + " <:RemKiss:656439154225315850>")
		elif message.author.id == 279550029981548545 and "аморал бака" in message.content.lower():
			await message.channel.send("дя! <:LewdMegumin:656439081747873802> ")
		elif message.author.id == 306125994396483587 and "тоша бака" in message.content.lower():
			await message.channel.send("дя! <:remhmpf:652885984115163196>")

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
	@commands.command(aliases=["yes"])
	async def Yes(self, ctx,):

		Yes = ["Да","+"]
		await ctx.send(f"{random.choice(Yes)}")

	@commands.command(aliases=["povtor".lower()])
	async def Povtor(self, ctx, *, arg,):

		await discord.Message.delete(ctx.message)
		await ctx.send(arg)

def  setup(client):
	client.add_cog(Hi(client))
