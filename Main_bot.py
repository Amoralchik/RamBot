"""RAM BOT 0.85 by Amoralchik."""

import asyncio
import functools
import itertools
import math
import os
import random
import discord
import youtube_dl
import json
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands , tasks

def get_prefix(bot, message):
	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	return prefixes[str(message.guild.id)]  

Version =  ("Версия: 0.85 // дата последнего обновления 20/12/2019")
status = cycle([ Version, "Няшется с цатиком", "Ждет ваших команд", "*setprefix"])

#Префикс вызова бота
bot = commands.Bot(command_prefix= get_prefix,
                   description=Version)

@tasks.loop(seconds=30)
async def change_status():
	await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
	change_status.start()
	print("Вход как: {0.user}".format(bot) + " Выполнен. " + Version )

@bot.event
async def on_guild_join(guild):
	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)
	
	prefixes[str(guild.id)] = "*"

	with open("prefixes.json", "w") as f:
		json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
	with open("prefixes.json","r") as f:
		prefixes = json.load(f)
	
	prefixes.pop[str(guild.id)]

	with open("prefixes.json","w") as f:
		json.dump(prefixes, f, indent=4)

for filename in os.listdir("./Cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"Cogs.{filename[:-3]}")

Token = os.environ.get("BOT_TOKEN")

bot.run(str(Token))
