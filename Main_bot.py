"""
Amoral BOT 0.95 by Amoralchik
2019-2020 (С)
2019 - RamBot - Last verison 0.85
"""

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
from TOKEN import BOT_TOKEN

def get_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]

Version =  ("Version: 0.95 // Last Update: 07/02/2020")

bot = commands.Bot(command_prefix= get_prefix,
                   description=Version)

bot.remove_command("help")

@tasks.loop(seconds=60)
async def change_status():
    userslist = ([user.id for user in bot.users])
    status = cycle(["with " + str(len(userslist)) + " member", Version, "with  @AMORALCHIK#1613", "with @Bl00dWolf#0001"])
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    userslist = ([user.id for user in bot.users])
    guildslist = ([guild.id for guild in bot.guilds])

    change_status.start()
    print("Logged in as: {0.user}".format(bot) + " Done. \n" + Version )

    print("All users: " + str(len(userslist)) + " | " + "All guilds: " + str(len(guildslist)))

@bot.event
async def on_guild_join(guild):
	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)
	
	prefixes[str(guild.id)] = "Amo."

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

bot.run(BOT_TOKEN)
