import os
import asyncio

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("Database/.env")

client = commands.Bot(
    command_prefix = ">",
    intents = discord.Intents.all(),
    help_command = None,
    strip_after_prefix = True,
    case_insensitive = True
)

extensions = []

for filename in os.listdir("./Cogs"):

    if filename.endswith(".py"):
        extensions.append(f"Cogs.{filename[:-3]}")

async def load_extensions() -> None:

    for extension in extensions:
        await client.load_extension(extension)

@client.event
async def on_ready() -> None:

    await client.tree.sync()
    print(f"Logged in as {client.user}")

async def main() -> None:

    await load_extensions()
    await client.start(os.getenv("BOT_TOKEN"))

asyncio.run(main())
