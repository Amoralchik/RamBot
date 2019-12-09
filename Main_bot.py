"""RAM BOT 0.050 by Amoralchik.""" 

import asyncio
import functools
import itertools
import math
import os
import random
import discord
import youtube_dl
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands , tasks
from TOKEN import BOT_TOKEN

status = cycle(["Верисия:0.050", "Няшется с цатиком", "Ждет ваших команд"])

#Префикс вызова бота
bot = commands.Bot(command_prefix=commands.when_mentioned_or("+"),
                   description='???')

@tasks.loop(seconds=50)
async def change_status():
	await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
	change_status.start()
	print("Вход как: {0.user}".format(bot) + " Выполнен." )

for filename in os.listdir("./Cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"Cogs.{filename[:-3]}")

bot.run(BOT_TOKEN)
