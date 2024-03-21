import logging
from Configs.av_utils import generate_avatar_embed

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
        
        await ctx.send(embed = generate_avatar_embed(ctx, user))

    # Error Handler

    @avatar.error
    async def avatar_error(self, ctx: commands.Context, error: commands.CommandError) -> None:

        if isinstance(error, commands.BadArgument):
            logging.error(error)
            await ctx.reply("Please check your inputs and try again.")

        else:
            logging.error(error)
            await ctx.send(":(\n\nAn unknown error occurred during the command execution.\n"
                        "To know further about the error info.. use the `>logs` command to fetch the `events.log` "
                        "file from the database!")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Avatar(client))