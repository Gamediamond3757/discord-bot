import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
name="ping",
description="ping pong"
)
async def first_command(interaction):
    await interaction.response.send_message("Pong!")
@tree.command(
name="info",
description="info about the bot"
)
async def first_command(interaction):
    await interaction.response.send_message("hosted on force host's snelheid server!")
@client.event
async def on_ready():
    await tree.sync()
    print("started")
    
client.run('token here')
