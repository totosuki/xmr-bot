import discord
import config

TOKEN = config.TOKEN

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("起動しました")

@client.event
async def on_message(message: discord.Message):
    print(message.author)
    if message.author.bot:
        return
    
    if message.content == '/hello':
        await message.channel.send('こんにちは！')

client.run(TOKEN)