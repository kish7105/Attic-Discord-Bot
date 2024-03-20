import datetime

import discord
from discord import app_commands
from discord.ext import commands

class Avatar(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name = "avatar", description = "Displays an user's avatar!", aliases = ["av"])
    @app_commands.describe(user = "Whose avatar do you wanna see?")
    @commands.guild_only()
    async def avatar(self, ctx: commands.Context, user: discord.Member = None) -> None:
        
        if user is None:
            embed = discord.Embed(
                color = discord.Color.random(),
                timestamp = datetime.datetime.now()
            )

            embed.set_author(name = f"{ctx.author.name}'s Discord PFP!")
            embed.set_image(url = ctx.author.avatar.url)

            await ctx.send(embed = embed)

        else:
            embed = discord.Embed(
                color = discord.Color.random(),
                timestamp = datetime.datetime.now()
            )

            embed.set_author(name = f"{user.name}'s Discord Avatar!")
            embed.set_image(url = user.avatar.url)

            await ctx.send(embed = embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Avatar(client))