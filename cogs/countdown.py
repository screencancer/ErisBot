import time
import pytz
import datetime
import discord

from discord.ext import commands


class Countdown(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def settime(self, ctx, month, day, year, time2):
        m, h = time2.split(':')
        m = int(m)
        h = int(h)
        month = int(month)
        day = int(day)
        year = int(year)

        endtime = datetime.datetime(year, month, day, h, m)
        print(endtime)


def setup(client):
    client.add_cog(Countdown(client))