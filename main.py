import discord
import config

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('XMRボットがログインしました') 
    await tree.sync()

@tree.command (
    name='hello',
    description='Say hello to the world!'
) 
async def test(interaction: discord.Interaction): 
    await interaction.response.send_message('Hello, World!')

client.run(config.TOKEN)