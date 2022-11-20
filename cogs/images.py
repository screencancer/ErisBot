import discord
import PIL
import PIL.Image
import io

from discord.ext import commands
from PIL import ImageDraw, ImageFilter, ImageOps
import requests

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)


class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slap(self, ctx, member : discord.Member):
        batslap = discord.File('./cogs/ImageFolder/batslap.png')
        id = ctx.message.author
        pfp = id.avatar.url
        size = 350, 350
        mentionedpfp = member.avatar.url

        mask = PIL.Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)

        img1 = PIL.Image.open('./cogs/ImageFolder/batslap.png')
        img2 = PIL.Image.open(requests.get(pfp, stream = True).raw)
        img3 = PIL.Image.open(requests.get(mentionedpfp, stream=True).raw)

        img2 = img2.resize(size)
        img3 = img3.resize(size)

        back_img = img1.copy()
        back_img.paste(img2, (484, 33), mask)
        back_img.paste(img3, (803, 302), mask)
        with io.BytesIO() as image_binary:
            back_img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.message.channel.send(file=discord.File(fp=image_binary, filename='batslap.png'))

    @commands.command()
    async def jail(self, ctx, member: discord.Member):
        jailimg = PIL.Image.open('./cogs/ImageFolder/jail.png')

        mask = jailimg.convert('L')
        size = 750,  750
        jailimg = jailimg.resize(size)

        pfp = member.avatar.url
        img2 = PIL.Image.open(requests.get(pfp, stream=True).raw)

        img2 = img2.convert('RGBA')
        jailimg = jailimg.convert('RGBA')
        mask = mask.convert('RGBA')

        mask = mask.resize(size)
        img2 = img2.resize(size)

        img23 = PIL.Image.composite(jailimg, img2, mask)

        back_img = img2.copy()
        back_img.paste(img23, jailimg)
        with io.BytesIO() as image_binary:
            back_img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.message.channel.send(file=discord.File(fp=image_binary, filename='jail.png'))

    @commands.command()
    async def podium(self, ctx, *members : discord.Member):
        if len(members) == 3:
            member1 = members[0]
            member2 = members[1]
            member3 = members[2]

        podiumimg = PIL.Image.open('./cogs/ImageFolder/podium.png')

        size = 147, 147
        sizemid = 225, 225
        sizethird = 143, 143

        mask = PIL.Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)

        pfp1 = member1.avatar.url
        pfp2 = member2.avatar.url
        pfp3 = member3.avatar.url

        img1 = PIL.Image.open(requests.get(pfp1, stream=True).raw)
        img2 = PIL.Image.open(requests.get(pfp2, stream=True).raw)
        img3 = PIL.Image.open(requests.get(pfp3, stream=True).raw)

        pfp1 = img1.resize(sizemid)
        pfp2 = img2.resize(size)
        pfp3 = img3.resize(sizethird)

        mask1 = mask.resize(sizemid)
        mask2 = mask.resize(size)
        mask3 = mask.resize(sizethird)

        bg_img = podiumimg.copy()
        bg_img.paste(pfp1, (270, 76), mask1)
        bg_img.paste(pfp2, (62, 155), mask2)
        bg_img.paste(pfp3, (563, 157), mask3)
        with io.BytesIO() as image_binary:
            bg_img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.message.channel.send(file=discord.File(fp=image_binary, filename='podium.png'))


async def setup(client):
    await client.add_cog(Image(client))
