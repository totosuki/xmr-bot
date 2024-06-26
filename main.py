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

@tree.command(
    name = "xmr-hashrate",
    description = "平均ハッシュレートを表示する hour = 0 にすると現在のハッシュレートを表示する"
)
async def xmr_hashrate(interaction: discord.Interaction, hour: int = 2):
    await interaction.response.defer()
    hashrate = xmr.return_hashrate(hour)
    if hour:
        await interaction.followup.send(f"過去{hour}時間の平均ハッシュレートは{hashrate:.2f}H/sです")
    else:
        await interaction.followup.send(f"現在のハッシュレートは{hashrate:.2f}H/sです")

client.run(config.TOKEN)
