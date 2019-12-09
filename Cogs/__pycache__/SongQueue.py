import asyncio
import functools
import itertools
import math
import discord
import youtube_dl
import os
import random
from async_timeout import timeout
from discord.ext import commands , tasks
from itertools import cycle

class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]

def  setup(client):
    client.add_cog(SongQueue(client))