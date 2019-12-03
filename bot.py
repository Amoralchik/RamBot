import discord
import os
import random
from discord.ext import commands

#Префикс вызова бота
client = commands.Bot(command_prefix='+')

@client.event
async def on_ready():
	print("Вход как: {0.user}".format(client) + " Выполнен." )

for filename in os.listdir("./Cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"Cogs.{filename[:-3]}")

client.run("MzA4NjE1MjExNDYyNDI2NjI1.XeKPvA.0n4j7s8VzfmZ0e36UuL3e4fS_zQ")
