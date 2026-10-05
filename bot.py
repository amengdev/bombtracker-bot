import os

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]
GUILD = discord.Object(id=int(os.environ["GUILD_ID"]))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "ping", description= " Checks that bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")


@client.event
async def on_ready():
    tree.copy_global_to(guild = GUILD)
    await tree.sync(guild=GUILD)
    print(f"Logged in as {client.user}")

client.run(TOKEN)