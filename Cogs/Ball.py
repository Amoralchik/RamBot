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

class Ball(commands.Cog):
	#Класс 2
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

	#команда для вопросов
	@commands.command(aliases=["8ball","8"])
	async def _8ball(self, ctx, *, question):
		""" "8ball","8" типичный 8балл"""
		responses = ["Бесспорно",
            		 "Предрешено",
            		 "Никаких сомнений",
            		 "Определённо да",
            		 "Можешь быть уверен в этом",
            		 "Мне кажется — «да»",
            		 "Вероятнее всего",
            		 "Хорошие перспективы",
            		 "Знаки говорят — «да»",
            		 "Да",
            		 "Пока не ясно, попробуй снова",
            		 "Спроси позже",
            		 "Лучше не рассказывать",
            		 "Сейчас нельзя предсказать",
            		 "Сконцентрируйся и спроси опять",
            		 "Даже не думай",
            		 "Мой ответ — «нет»",
            		 "По моим данным — «нет»",
            		 "Перспективы не очень хорошие",
            		 "Весьма сомнительно"]
		
		choice = {random.choice(responses)}

		emb= discord.Embed( colour=discord.Colour.magenta())
		emb.add_field(name= "**{0}**".format(question), value=  " ".join(choice))
		emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

		await ctx.send(embed= emb)

	#простая команда вывода да/нет
	@commands.command(aliases=["данет","нетда","yesornot"])
	async def Yesornot(self, ctx, *, question):
		""" "данет","нетда","yesornot" говорит да/нет"""
		
		Yesornot = ["Да","Нет"]

		choice = {random.choice(Yesornot)}

		emb= discord.Embed( colour=discord.Colour.magenta())
		emb.add_field(name= "**{0}**".format(question), value= " ".join(choice))
		emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

		await ctx.send(embed= emb)

	@commands.command()
	async def choose(self, ctx, *args):
		""" args """
		
		emb= discord.Embed( colour=discord.Colour.magenta())
		emb.add_field(name= "<:KannaSip:669635038089838602>", value= "{0}".format({random.choice(args)}))
		emb.set_footer(text= "Requested by {}".format(ctx.author), icon_url= ctx.author.avatar_url)

		await ctx.send(embed= emb)

def  setup(client):
	client.add_cog(Ball(client))