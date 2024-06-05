import discord
import config
import xmr

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

@tree.command(
    name = "xmr-balance",
    description = "現在のXMR残高を日本円で表示する"
)
async def xmr_balance(interaction: discord.Interaction):
    await interaction.response.defer()
    balance = xmr.return_balance()
    await interaction.followup.send(f"現在のXMR残高は{balance:.2f}円です")

client.run(config.TOKEN)