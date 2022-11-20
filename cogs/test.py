import discord
from discord.ext import commands
from discord import app_commands


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')


async def setup(client):
    await client.add_cog(Test(client))


