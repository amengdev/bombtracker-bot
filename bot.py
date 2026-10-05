import os

import discord
from discord import app_commands
from dotenv import load_dotenv

from datetime import datetime
import aiohttp

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]
GUILD = discord.Object(id=int(os.environ["GUILD_ID"]))
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8080")

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


@tree.command(name = "bombs", description="Lists currently active bombs")
async def bombs(interaction: discord.Interaction):
    await interaction.response.defer()

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{BACKEND_URL}/bombs/active", timeout= aiohttp.ClientTimeout(total=5)) as resp:

                resp.raise_for_status()
                data = await resp.json()
    except Exception:
        await interaction.followup.send("Could not reach backend.")
        return
    if not data:
        await interaction.followup.send("No active bombs right now.")

    lines = []
    for bomb in data:
        expires = datetime.fromisoformat(bomb["expiresAt"])
        player = discord.utils.escape_markdown(bomb["player"])
        lines.append(f"**{bomb['type']}** on **{bomb['server']}** by {player}, " f"ends <t:{int(expires.timestamp())}:R>")

    await interaction.followup.send("\n".join(lines))
client.run(TOKEN)