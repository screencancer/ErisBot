import discord
import os
import logging
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("DISCORD_API_TOKEN")


from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='.', intents=intents, help_command=None)

status = cycle(['.help for commands', 'Hello'])

#logs bot for debugging purposes

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@client.event
async def on_ready():
    change_status.start()
    print("Bot is Ready")
    await client.change_presence(status = discord.Status.online)


@tasks.loop(seconds = 600)
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


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    else:
        continue


@client.command()
async def help(ctx):
    embed1 = discord.Embed(title="Help", description="Commands with Example usage",color=0x00ff00)
    embed1.add_field(name="Countdown", value=".countdown Example_Name 5/31/2021 12:56 AM PST\n .stop(stops countdown)", inline=False)
    embed1.add_field(name="Image Generation", value=".jail @user\n.podium @1stUser @2ndUser @3rdUser\n.slap @user",inline=False)
    embed1.add_field(name="Random", value=".8ball Example question here",inline=False)
    await ctx.send(embed=embed1)

client.run(bot_token)