import datetime

import discord
from discord import Embed
from discord.ext import commands

def generate_avatar_embed(ctx: commands.Context, user: discord.Member = None) -> Embed:

    """Generates a `discord.Embed` object which is used for the avatar command in `avatar.py` file.
    
    ## Parameters
    
    ctx: `commands.Context`
        Holds information regarding the command invocation.
        
    user: `discord.Member`
        For obtaining the avatar of a particular user. This defaults to `None` if the author wants to
        see their profile's avatar."""
    
    if user is None:  # if the author wants to see their profile picture
    
        embed = Embed(
            color = discord.Color.random(),
            timestamp = datetime.datetime.now()
        )

        embed.set_author(name = f"{ctx.author.name}'s Discord PFP!")
        embed.set_image(url = ctx.author.avatar.url)

        return embed

    else:  # if the author wants to see someone else's profile picture

        embed = Embed(
            color = discord.Color.random(),
            timestamp = datetime.datetime.now()
        )

        embed.set_author(name = f"{user.name}'s Discord PFP!")
        embed.set_image(url = user.avatar.url)

        return embed