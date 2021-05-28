import time
import pytz
import datetime as dt
import discord

from pytz import timezone
from pytz import common_timezones
from discord.ext import commands

Tz = {
    'PST': timezone('America/Los_Angeles'),
    'CEST': timezone('Europe/Berlin'),
    'EST': timezone('America/New_York'),
    'UTC': pytz.utc
}
# UTC = pytz.utc
# CEST = timezone('Europe/Berlin')
# PST = timezone('America/Los_Angeles')
# EST = timezone('America/New_York')
# print(CEST.zone, UTC.zone, PST.zone, EST.zone)


class Countdown(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def settime(self, ctx, month, day, year, time2, timezone1):

        h, m = time2.split(':')
        m = int(m)
        h = int(h)
        month = int(month)
        day = int(day)
        year = int(year)

        # timezoneend = pytz.timezone(Tz[timezone1])
        date = dt.datetime(year, month, day, h, m,)
        print(date)
        cur_date = dt.datetime.now(Tz[timezone1])
        print(cur_date)


def setup(client):
    client.add_cog(Countdown(client))