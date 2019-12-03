import discord
import os
import random
from discord.ext import commands

class Hi(commands.Cog):
#Класс 1
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	@commands.Cog.listener()
	async def on_message(self, message):
	# уже работает, и говорит привет на привет =_=

		if message.content == 'Привет рем':
			await message.channel.send("Привет няш <:love:443438912258703371>")
		elif message.content == 'Привет Рем':
			await message.channel.send("Привет няш <:love:443438912258703371>")
		elif message.content == 'Привет Рем чян':
			await message.channel.send("Привет няш <:love:443438912258703371>")
		elif message.content == 'Привет рем чян':
			await message.channel.send("Привет няш <:love:443438912258703371>")
		elif message.content == 'привет рем':
			await message.channel.send("Привет няш <:love:443438912258703371>")
		elif message.content == 'привет рем чян':
			await message.channel.send("Привет няш <:love:443438912258703371>")

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send('Приветик {0.mention}.'.format(member))

	""" @commands.command(aliases=["Привет","привет"])
				async def hello(self, ctx, *, member: discord.Member = None):
					"" Отвечает приветом на привет ""
					member = member or ctx.author
					if self._last_member is None or self._last_member.id != member.id:
						await ctx.send('Привет {0.name}~'.format(member))
					else:
						await ctx.send('Привет {0.name}... Кажется ты уже это делал.'.format(member))
					self._last_member = member """

def  setup(client):
	client.add_cog(Hi(client))