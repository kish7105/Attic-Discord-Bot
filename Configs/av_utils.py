import datetime

import discord
from discord import Embed
from discord.ext import commands

def generate_avatar_embed(ctx: commands.Context, user: discord.Member = None) -> Embed:
    
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