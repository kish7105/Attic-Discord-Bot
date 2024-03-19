import os
import asyncio
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("Database/.env")

logging.basicConfig(
    filename = "Database/events.log",
    filemode = "w",
    level = logging.INFO,
    format = "[%(levelname)s] | %(asctime)s - %(message)s [Line: %(lineno)s %(filename)s]",
    datefmt = "%I:%M:%S %p"
)

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

@client.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
    
    if isinstance(error, commands.BadArgument):
        await ctx.reply("An error occurred while executing the command.\n"
                        "Please check your inputs before trying out the command again!")
        logging.error(error)
        return
    
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("An error occurred while executing the command.\n"
                        "Please check if you provided the correct number of inputs before trying again!")
        logging.error(error)
        return
    
    else:
        logging.error(error)
        
        await ctx.send(":(\n\nOops\nAn error occurred during the command execution.\n"
                    "Please check the `log file` attached with this message to debug the error!",
                    file = discord.File("Database/events.log"))

async def main() -> None:

    await load_extensions()
    await client.start(os.getenv("BOT_TOKEN"))

asyncio.run(main())
