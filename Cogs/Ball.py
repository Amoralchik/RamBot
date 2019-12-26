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
		await ctx.send(f"Вопрос: {question} \n Ответ: {random.choice(responses)}")

	#простая команда вывода да/нет
	@commands.command(aliases=["данет","нетда","yesornot"])
	async def Yesornot(self, ctx, *, question):
		""" "данет","нетда","yesornot" говорит да/нет"""
		Yesornot = ["Да","Нет"]
		await ctx.send(f"Вопрос: {question} \n {random.choice(Yesornot)}")

def  setup(client):
	client.add_cog(Ball(client))