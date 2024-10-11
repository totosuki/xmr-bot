import discord
import config
import xmr
from others.Data import Address, Balance, Hashrate, Help, Member

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('XMRボットがログインしました') 
    await tree.sync()

@tree.command(
    name = Address.name,
    description = Address.description
)
async def xmr_address(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(title=Address.title, description=config.ADDRESS, color=config.GREEN)
    await interaction.followup.send(embed=embed)

@tree.command(
    name = Balance.name,
    description = Balance.description
)
async def xmr_balance(interaction: discord.Interaction):
    await interaction.response.defer()
    balance = xmr.return_balance()
    embed = discord.Embed(title=Balance.title, description=f"現在のXMR残高は{balance:.2f}円です", color=config.GREEN)
    await interaction.followup.send(embed=embed)

@tree.command(
    name = Hashrate.name,
    description = Hashrate.description
)
async def xmr_hashrate(interaction: discord.Interaction, hour: int = 2, member: str = ""):
    await interaction.response.defer()
    hashrate = xmr.return_hashrate(hour, member)
    embed = discord.Embed(title=Hashrate.title, description=Hashrate.embed_description(hour, member, hashrate), color=config.GREEN)
    await interaction.followup.send(embed=embed)

@tree.command(
    name=Help.name,
    description=Help.description
)
async def xmr_help(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(title=Help.title, description="XMRボットのコマンド一覧です", color=config.GREEN)
    embed.add_field(name=Balance.name, value="現在のXMR残高を日本円で表示する", inline=False)
    embed.add_field(name=Hashrate.name, value="平均ハッシュレートを表示する\n`hour = 0` にすると現在のハッシュレートを表示する", inline=False)
    embed.add_field(name=Help.name, value="XMRボットのヘルプを表示する", inline=False)
    embed.add_field(name=Address.name, value="設定されているXMRのアドレスを表示する", inline=False)
    embed.add_field(name=Member.name, value="現在マイニング中のメンバーを表示する", inline=False)
    await interaction.followup.send(embed=embed)

@tree.command(
    name=Member.name,
    description=Member.description
)
async def xmr_member(interaction: discord.Interaction):
    await interaction.response.defer()
    member_list = xmr.return_member()
    embed = discord.Embed(title=Member.title, color=config.GREEN)
    for i in range(len(member_list)):
        embed.add_field(name=f"{member_list[i]}", value="")
    await interaction.followup.send(embed=embed)

client.run(config.TOKEN)
