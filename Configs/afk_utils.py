import time
import datetime

import discord
from discord import Embed
from discord.ext import commands

def generate_afk_embed(ctx: commands.Context, reason: str) -> Embed:

    """Generates a `discord.Embed` object for the afk command in `afk.py` file
    
    ## Parameters
    
    ctx: `commands.Context`
        Holds information about the command invocation.
        
    reason: `str`
        This is provided by the command author during command invocation."""

    embed = discord.Embed(
        description = f"{ctx.author.name} went AFK <t:{int(time.time())}:R>",
        color = discord.Color.random(),
        timestamp = datetime.datetime.now()
        )

    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar.url)
    embed.add_field(name = "Reason:", value = f"```{reason}```", inline = False)

    return embed