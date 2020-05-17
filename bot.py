import discord
import config as Config
import random
from discord.ext import commands, tasks
import asyncio
import rssreader as postman

client = discord.Client()
TOKEN = Config.getToken()
GUILD = int(Config.getGuild())
CH = int(Config.getMusik())

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.channel = self.bot.get_channel(CH)
        self.pm = postman.Postman()
        self.printer.start()
        

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        msg = self.pm.getPosts()
        await self.bot.do_message(msg)

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()

class CustomClient(discord.Client):

    @client.event
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    @client.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )

    @client.event
    async def do_message(self, msg):
        if msg is not "nothing":
            channel = self.get_channel(CH)
            await channel.send(msg)
        else:
            print("nada")
            
    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        if message.content == '^99':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)
    
client = CustomClient()
cog = MyCog(client)
client.run(TOKEN)

