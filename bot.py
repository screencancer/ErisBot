import discord
import os

from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='.', intents=intents)
status = cycle(['.help for commands', 'Hello'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
    await client.change_presence(status = discord.Status.online)


@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded')


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODQyNDMzMDE0NjkyNTc3MzMy.YJ1O4g.jj4j7KyCuzToY9QAJW0bohKSzLM')
