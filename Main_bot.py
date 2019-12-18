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

Version =  ("Версия: 0.60 // дата последнего обновления 17/12/2019")
status = cycle([ Version, "Няшется с цатиком", "Ждет ваших команд", "+help"])

#Префикс вызова бота
bot = commands.Bot(command_prefix=commands.when_mentioned_or("+"),
                   description=Version)

@tasks.loop(seconds=30)
async def change_status():
	await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
	change_status.start()
	print("Вход как: {0.user}".format(bot) + " Выполнен. " + Version )

for filename in os.listdir("./Cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"Cogs.{filename[:-3]}")

Token = os.environ.get("BOT_TOKEN")

bot.run(str(Token))
