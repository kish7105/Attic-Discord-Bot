import discord
from discord.ext import commands


client = commands.Bot(
    command_prefix = ">",
    intents = discord.Intents.all(),
    help_command = None,
    strip_after_prefix = True,
    case_insensitive = True
)


@client.event
async def on_ready() -> None:

    await client.tree.sync()
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    pass


client.run("INSERT BOT TOKEN HERE")
