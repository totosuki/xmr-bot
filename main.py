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
    name="xmr-help",
    description="XMRボットのヘルプを表示する"
)
async def xmr_help(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(title="XMRボットのヘルプ", description="XMRボットのコマンド一覧です", color=config.GREEN)
    embed.add_field(name="xmr-balance", value="現在のXMR残高を日本円で表示する", inline=False)
    embed.add_field(name="xmr-hashrate hour(default=2)", value="平均ハッシュレートを表示する\n`hour = 0` にすると現在のハッシュレートを表示する", inline=False)
    embed.add_field(name="xmr-help", value="XMRボットのヘルプを表示する", inline=False)
    await interaction.followup.send(embed=embed)

@tree.command(
    name = "xmr-balance",
    description = "現在のXMR残高を日本円で表示する"
)
async def xmr_balance(interaction: discord.Interaction):
    await interaction.response.defer()
    balance = xmr.return_balance()
    embed = discord.Embed(title="XMR残高", description=f"現在のXMR残高は{balance:.2f}円です", color=config.GREEN)
    await interaction.followup.send(embed=embed)

@tree.command(
    name = "xmr-hashrate",
    description = "平均ハッシュレートを表示する hour = 0 にすると現在のハッシュレートを表示する"
)
async def xmr_hashrate(interaction: discord.Interaction, hour: int = 2):
    await interaction.response.defer()
    hashrate = xmr.return_hashrate(hour)
    if hour:
        embed = discord.Embed(title="XMRハッシュレート", description=f"過去{hour}時間の平均ハッシュレートは{hashrate:.2f}H/sです", color=config.GREEN)
    else:
        embed = discord.Embed(title="XMRハッシュレート", description=f"現在のハッシュレートは{hashrate:.2f}H/sです", color=config.GREEN)
    await interaction.followup.send(embed=embed)

client.run(config.TOKEN)
